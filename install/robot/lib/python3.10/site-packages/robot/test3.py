import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel
from dynamixel_sdk import *
from robot.ik import fcn
from std_msgs.msg import String
import threading
import time
import os


PROTOCOL_VERSION = 2.0
ADDR_TORQUE_ENABLE = 64
ADDR_GOAL_POSITION = 116
ADDR_PRESENT_POSITION = 132
ADDR_GOAL_VELOCITY = 112
ADDR_PRES_VELOCITY = 104

BAUDRATE = 115200
DEVICE_NAME = "/dev/ttyUSB0"
portHandler = PortHandler(DEVICE_NAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

LEN_PRO_LED_RED             = 1
LEN_PRO_GOAL_POSITION       = 4
LEN_PRO_PRESENT_POSITION    = 4

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

DXL1_ID,DXL2_ID,DXL3_ID,DXL4_ID,DXL5_ID,DXL6_ID = 1,2,3,4,5,6

min1, max1 = 200, 4400
min2, max2 = 1024, 3070
min3, max3 = 700, 3360
min4, max4 = 0, 4095
min5, max5 = 1300, 3000
min6, max6 = 0, 4095
rad = 3.14159265359 / 180

def ang(a1,a2,a3,a4,a5,a6):
    q1,q2,q3,q4,q5,q6 = fcn(a1,a2,a3,a4,a5,a6)
    q1=q1/rad
    q2=q2/rad
    q3=q3/rad
    q4=q4/rad
    q5=q5/rad
    q6=q6/rad
    #print(q1,q2,q3,q4,q5,q6)
    pos1 = q1*4096/360
    pos2 = q2*4096/360
    pos3 = q3*4096/360
    pos4 = q4*4096/360
    pos5 = q5*4096/360
    pos6 = int(q6*4096/360)

    pos1 = int(pos1 + 2500.0)
    pos2 = int((pos2* 952 / 1024) + 1096.0)
    pos3 = int(-pos3 + 2048.0)
    pos4 = int(pos4 + 1948.0)
    pos5 = int(pos5 + 2500.0)
            
    if pos1 < min1:
        pos1 = min1
    elif pos1 > max1:
        pos1 = max1

    if pos2 < min2:
        pos2 = min2
    elif pos2 > max2:
        pos2 = max2

    if pos3 < min3:
        pos3 = min3
    elif pos3 > max3:
        pos3 = max3

    if pos4 < min4:
        pos4 = min4
    elif pos4 > max4:
        pos4 = max4

    if pos5 < min5:
        pos5 = min5
    elif pos5 > max5:
        pos5 = max5

    if pos6 < min6:
        pos6 = min6
    elif pos6 > max6:
        pos6 = max6
         
    print(pos1)
    return pos1,pos2,pos3,pos4,pos5,pos6

def initial_pos():
    # q1,q2,q3,q4,q5,q6 = fcn(0,0,550,-90,0,0)
    lis = list(ang(0,0,600,90,0,0))
    print(lis)
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
        time.sleep(0.1)
        #print(lis[i-1])
       
       
def open(task):
    if task==0:
        packetHandler.write4ByteTxRx(portHandler, 7, 104, -230)
        prt=time.time()
        while(time.time()-prt)<1.5:
            print("opening ",read_pos(7))
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
        
    if task==1:
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 230)
        prt=time.time()
        while(time.time()-prt)<1.5:
            print("opening ",read_pos(7))
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
       
def pick(coor,color='grn'):
    first = read_pos(7)
    lis =  list(ang(200,0,350,-90,0,70))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    while(True):
        if abs(read_pos(1)-lis[0])<20 and abs(read_pos(2)-lis[1])<35 and abs(read_pos(3)-lis[2])<50 and abs(read_pos(4)-lis[3])<20 and abs(read_pos(5)-lis[4])<20:
            break
        else:
            print(abs(read_pos(1)-lis[0]),abs(read_pos(2)-lis[1]),abs(read_pos(3)-lis[2]),abs(read_pos(4)-lis[3]), abs(read_pos(5)-lis[4]))
    print(110)
    open(0)
    print("open ",read_pos(7))
    lis =  list(ang(280,coor,310,-90,0,70))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    while(True):
        if abs(read_pos(1)-lis[0])<20 and abs(read_pos(2)-lis[1])<35 and abs(read_pos(3)-lis[2])<55 and abs(read_pos(4)-lis[3])<20 and abs(read_pos(5)-lis[4])<20:
            break
        else:
            print(abs(read_pos(1)-lis[0]),abs(read_pos(2)-lis[1]),abs(read_pos(3)-lis[2]),abs(read_pos(4)-lis[3]), abs(read_pos(5)-lis[4]))
            
    time.sleep(2)
    open(1)
    qth2=1680+300
    lis=[qth2,2700]
    idss=1
    for i in lis:
        idss+=1
        packetHandler.write4ByteTxRx(portHandler, idss, ADDR_GOAL_POSITION, i)
    while(True):
        if abs(read_pos(2)-qth2)<35:
            break
    if color=='red':
        qth1=3700
    elif color=='grn':
        qth1=1500
    lis=[qth1]
    idss=0
    for i in lis:
        idss+=1
        packetHandler.write4ByteTxRx(portHandler, idss, ADDR_GOAL_POSITION, i)
    while(True):
        if abs(read_pos(1)-qth1)<30:
            break
    
    qth2=read_pos(2)-300
    lis=[qth2]
    idss=1
    for i in lis:
        idss+=1
        packetHandler.write4ByteTxRx(portHandler, idss, ADDR_GOAL_POSITION, i)
    while(True):
        if abs(read_pos(2)-qth2)<35:
            break
    open(0)
    open(1)
    qth2=read_pos(2)+300
    lis=[qth2]
    idss=1
    for i in lis:
        idss+=1
        packetHandler.write4ByteTxRx(portHandler, idss, ADDR_GOAL_POSITION, i)
    while(True):
        if abs(read_pos(2)-qth2)<35:
            break
    if read_pos(1)>2048:
        qth1=read_pos(1)-700
    else:
        qth1=read_pos(1)+700
    lis=[qth1]
    idss=0
    for i in lis:
        idss+=1
        packetHandler.write4ByteTxRx(portHandler, idss, ADDR_GOAL_POSITION, i)
    while(True):
        if abs(read_pos(1)-qth1)<30:
            break
            
    '''
    while(True):
        second=read_pos(7)
        if second>900000:
            second-=4294967295
        if second>first:
            break
        print("closing ",second)
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 230)
    packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
    print(3)
    '''
    #red()
    #'''
    lis =  list(ang(200,0,350,-90,0,70))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(2)
    #'''
def green():
    lis =  list(ang(-0,200,350,-90,0,0))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(3)
    first = read_pos(7)
    open()
    while(True):
        second=read_pos(7)
        if second>900000:
            second-=4294967295
        if second>first:
            break
        print("closing ",second)
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 230)
    packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
    lis =  list(ang(200,0,350,-90,0,70))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(3)
    
def orange():
    lis =  list(ang(-200,00,350,-90,0,0))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(3)
    first = read_pos(7)
    open()
    while(True):
        second=read_pos(7)
        if second>900000:
            second-=4294967295
        if second>first:
            break
        print("closing ",second)
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 230)
    packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
    lis =  list(ang(200,0,350,-90,0,70))
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(3)
    
def red():
    q1,q2,q3,q4,q5,q6 = 110,90,-80,0,-90,0
    #print(q1,q2,q3,q4,q5,q6)
    pos1 = q1*4096/360
    pos2 = q2*4096/360
    pos3 = q3*4096/360
    pos4 = q4*4096/360
    pos5 = q5*4096/360
    pos6 = int(q6*4096/360)

    pos1 = int(pos1 + 2500.0)
    pos2 = int((pos2* 952 / 1024) + 1096.0)
    pos3 = int(-pos3 + 2048.0)
    pos4 = int(pos4 + 1948.0)
    pos5 = int(pos5 + 2500.0)
    
    lis=[pos1,pos2,pos3,pos4,pos5,pos6]
    print(lis)
    for i in range(1,7):
        packetHandler.write4ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
    time.sleep(3)
   
    first = read_pos(7)
    open(0)
    open(1)
    '''
    while(True):
        second=read_pos(7)
        if second>900000:
            second-=4294967295
        if second>first:
            break
        print("closing ",second)
        packetHandler.write4ByteTxRx(portHandler, 7, 104, 230)
    packetHandler.write4ByteTxRx(portHandler, 7, 104, 0)
    '''
#'''
def rest():
    res = [2425,1538,1600,2130,1250,1320]
    packetHandler.write4ByteTxRx(portHandler, 4, ADDR_GOAL_POSITION, res[3])
    packetHandler.write4ByteTxRx(portHandler, 5, ADDR_GOAL_POSITION, res[4])
    packetHandler.write4ByteTxRx(portHandler, 6, ADDR_GOAL_POSITION, res[5])
    packetHandler.write4ByteTxRx(portHandler, 1, ADDR_GOAL_POSITION, res[0])
    while (read_pos(1)-res[0])>30:
        pass
    packetHandler.write4ByteTxRx(portHandler, 3, ADDR_GOAL_POSITION, res[2])
    while (read_pos(3)-res[2])>30:
        pass
    packetHandler.write4ByteTxRx(portHandler, 2, ADDR_GOAL_POSITION, res[1])
    while (read_pos(2)-res[1])>30:
        pass
        
def ready():
    lis = list(fcn(100,0,300,-90,0,0))
    for i in range(1,7):
        packet_handler.write1ByteTxRx(portHandler, i, ADDR_GOAL_POSITION, lis[i-1])
        print(lis[i-1])   
                      
def read_pos(i):
    present_pos,dxl_comm_result,dxl_error = packetHandler.read4ByteTxRx(portHandler, i, ADDR_PRESENT_POSITION)
    return present_pos
    
def main(args=None):
    #present_pos = packetHandler.read4ByteTxRx(portHandler, i, ADDR_PRESENT_POSITION)
    
    while 1:
        packetHandler.write1ByteTxRx(portHandler, 7, ADDR_TORQUE_ENABLE, 0)
        packetHandler.write1ByteTxRx(portHandler, 7, 11, 1)
        packetHandler.write1ByteTxRx(portHandler, 7, ADDR_TORQUE_ENABLE, 1)
        for i in range(1,7):
            #packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 0)
            #packetHandler.write1ByteTxRx(portHandler, i, 11, 3)
            if i<4:
                packetHandler.write4ByteTxRx(portHandler, i, 112, 30)
            else:
                packetHandler.write4ByteTxRx(portHandler, i, 112, 50)
            packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 1)
        
        #for i in range(1,7):
        #    packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 0)
        #initial_pos()
        #time.sleep(3)
        #rest()
        #print(packetHandler.read4ByteTxRx(portHandler, 7, 126)[0])
        #print(65535 - packetHandler.read2ByteTxRx(portHandler, 7, 126)[0])

        pick(0,'red')
        break
        
    #green()
    #packetHandler.write1ByteTxRx(portHandler, 7, ADDR_TORQUE_ENABLE, 0)
    #packetHandler.write1ByteTxRx(portHandler, 6, ADDR_TORQUE_ENABLE, 0)
    #packetHandler.write1ByteTxRx(portHandler, 5, ADDR_TORQUE_ENABLE, 0)
if __name__ == '__main__':
    main()
