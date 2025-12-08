import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel
from dynamixel_sdk import *
from std_msgs.msg import String
import threading
import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
PROTOCOL_VERSION = 2.0
ADDR_TORQUE_ENABLE = 64
ADDR_GOAL_POSITION = 116
ADDR_PRESENT_POSITION = 132
ADDR_GOAL_VELOCITY = 112

BAUDRATE = 115200
DEVICE_NAME = "/dev/ttyUSB1"
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

min1, max1 = 500, 3800
min2, max2 = 1024, 3070
min3, max3 = 700, 3360
min4, max4 = 0, 4095
min5, max5 = 1000, 4000
min6, max6 = 0, 4095
prev1 = 0
prev2 = 0
prev3 = 0
prev4 = 0


# to read the current position of the dynamixel motor:
# present_pos,dxl_comm_result,dxl_error = packetHandler.read4ByteTxRx(portHandler, id, ADDR_PRESENT_POSITION)


flg=0
class SetPositionPublisher(Node):
    def __init__(self):
        super().__init__('set_position_publisher_n')
        self.subscription = self.create_subscription(Posvel, '/set_position_n',self.set_goal_pos_callback, 10)
        
    def set_goal_pos_callback(self,msg):
        global flg
        global prev1,prev2,prev3,prev4
        #self.get_logger().info(f"Set Goal Position of ID 1,2,3,4,5,6 = {msg.position1}, {msg.position2}, {msg.position3}")
        if (msg.position1==-1.234):
            if msg.torque==1:
                for i in range(1,7):
                    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 1)
                    print("Id -> ", i)
            elif msg.torque==0:
                for i in range(1,7):
                    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 0)
                    print("Id -> ", i)
        else:
            pos1 = msg.position1*4096/360
            pos2 = msg.position2*4096/360
            pos3 = msg.position3*4096/360
            pos4 = msg.position4*4096/360
            pos5 = (msg.position5)*4096/360
            #pos5 = pos5+115
            pos6 = int(msg.position6*4096/360)
            
            #print(pos2)
            pos1 = int(pos1 + 2500.0)
            pos2 = int((pos2* 952 / 1024) + 1096.0)
            pos3 = int(-pos3 + 2048.0)
            pos4 = int(pos4 + 2000.0)
            pos5 = int(pos5 + 2500.0)
            vel1 = 30 
            vel2 = 15 
            print(pos5)
            
            
            self.get_logger().info(f"Set Goal Position of ID 1,2,3,4,5,6 = {pos1}, {pos2}, {pos3}, {pos4}, {pos5}, {pos6}")
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
                
                
            if flg:
                print("hello",prev1,pos1)
                t1 = threading.Thread(target=move_smoothly,args=(1, prev1, pos1, 2000,))
                t1.start()
                #move_smoothly(1, prev1, pos1, 2000)
                
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 2, 112, int(vel2))
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 2, 116, pos2)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 3, 112, 30)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 3, 116, pos3)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 4, 112, 55)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 4, 116, pos4)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 5, 112, 55)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 5, 116, pos5)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 6, 112, 60)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 6, 116, pos6)
                
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, 1, ADDR_PRESENT_POSITION)
                print(dxl_present_position)
                prev1 = dxl_present_position
                prev2 = pos2
                prev3 = pos3
                prev4 = pos4
                
            else:
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 1, 112, int(vel1))
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 1, 116, pos1)
                
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 2, 112, int(vel2))
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 2, 116, pos2)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 3, 112, 30)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 3, 116, pos3)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 4, 112, 55)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 4, 116, pos4)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 5, 112, 55)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 5, 116, pos5)
	        
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 6, 112, 60)
                dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 6, 116, pos6)
                
     
                
def main(args=None):
    for i in range(1,7):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_TORQUE_ENABLE, 1)
    rclpy.init(args=args)
    set_position_publisher = SetPositionPublisher()
    rclpy.spin(set_position_publisher)
    set_position_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
