import numpy as np 
import cv2 
from numpy import ones,vstack
from numpy.linalg import lstsq
import math
import time 
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

lis=[]

class TomatoSubscriber(Node):
    def __init__(self):
        super().__init__('tomato_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'tomato_info',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print(msg)
        self.get_logger().info('Received: "%d"' % msg.data) 


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

prev_frame_time = 0
new_frame_time = 0

pt1 = (40, 230)
pt2 = (636, 214)
pt3 = (638, 277)
pt4 = (45, 293)


pts=[pt1,pt2,pt3,pt4]
pts_x=[]
pts_y=[]
for i in pts:
    pts_x.append(i[1])
    pts_y.append(i[0])
pts_x.sort()
pts_y.sort()

def mask_crop(img,pt1,pt2,pt3,pt4):
    y,x,_ = img.shape
    mask = np.zeros((y,x), np.uint8)
    triangle_cnt = np.array( [pt4, pt1, pt2, pt3] )
    cv2.drawContours(mask, [triangle_cnt], 0, 255, -1)
    img = cv2.bitwise_and(img, img, mask=mask)
    return img

def mask_grn(img):
    image=cv2.blur(img, (4,4))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (20, 70, 50), (30, 255, 255))
    target = cv2.bitwise_and(img,img, mask=mask)
    return mask

def mask_red(img):
    image=cv2.blur(img, (6,6))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 90, 50), (100, 255, 255))
    target = cv2.bitwise_and(img,img, mask=mask)
    return mask

def mask_org(img):
    image=cv2.blur(img, (4,4))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (10, 70, 50), (20, 255, 255))
    target = cv2.bitwise_and(img,img, mask=mask)
    return mask

def mask_neg(img):
    image=cv2.blur(img, (7,7))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, (50, 0, 0), (100, 255, 100))
    mask = cv2.inRange(hsv, (0, 60, 50), (200, 255, 255))
    # mask = cv2.bitwise_not(mask)
    target = cv2.bitwise_and(img,img, mask=mask)
    return target,mask


def main(args=None):    
    rclpy.init(args=args)
    node = TomatoSubscriber()
    while(cap.isOpened()): 
        ret, frame = cap.read()
        new_frame_time = time.time() 
        if ret:
            img_c=frame
            img_c=mask_crop(img_c,pt1,pt2,pt3,pt4)
            img_c=img_c[pts_x[0]:pts_x[-1],pts_y[0]:pts_y[-1],:]
            
            img_d=img_c.copy()
            # print(img.shape)
            img,thresh =mask_neg(img_c)
            contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            f=open("x.txt",'r')
            lis_x=list(map(float,f.read().split()))
            f.close()
            act_x=lis_x[0]
            '''
            f=open("x.txt",'w')
            for i in lis_x[1:]:
                f.write(str(i)+' ')
            f.close()
            '''
            for cnt in contours:
                act_y=0
                x,y,w,h = cv2.boundingRect(cnt)
                if(w*h>1000 and w*h<10000):
                    #img_t=img_c[y:y+h,x:x+w,:]
                    img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,0,255),3)
                    img_d = cv2.circle(img_d,(x+(w//2),y+(h//2)),0,(255,0,0),5)
                    act_y = x+(w//2)
                    print(act_y,act_x)
            #         img_rm=mask_red(img_t)
            #         img_om=mask_org(img_t)
            #         img_gm=mask_grn(img_t)
            #         mask=[np.sum(img_rm == 255),np.sum(img_om == 255),np.sum(img_gm == 255)]
            #         if mask.index(max(mask))==0:
            #             img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,0,255),4)
            #         elif mask.index(max(mask))==1:
            #             img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,165,255),4)
            #         elif mask.index(max(mask))==2:
            #             img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,255,0),4)
            #img =mask_red(img_c)
            
            #cv2.imshow('o_frame2',img_c) 
            #cv2.imshow('frame2', img) 
            cv2.imshow('frame21', img_d) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release() 
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    main()
