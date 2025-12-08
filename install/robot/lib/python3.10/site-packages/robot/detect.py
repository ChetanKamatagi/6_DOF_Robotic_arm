import numpy as np 
import cv2 
from numpy import ones,vstack
from numpy.linalg import lstsq
import math
import time 
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class TomatoPublisher(Node):
    def __init__(self):
        super().__init__('tomato_publisher')
        self.publisher_ = self.create_publisher(Int32, 'tomato_info', 10)

    def publish_tomato_info(self, color_id, x_coordinate):
        msg = Int32()
        msg.data = color_id
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d" with x-coordinate: "%d"' % (color_id, x_coordinate))

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

prev_frame_time = 0
new_frame_time = 0

pt1 = (0, 25)
pt2 = (319, 25)
pt3 = (319, 210)
pt4 = (0, 210)

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
    image=cv2.blur(img, (7,7))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (20, 0, 50), (35, 255, 255))
    target = cv2.bitwise_and(img,img, mask=mask)
    return mask

def mask_red(img):
    image=cv2.blur(img, (6,6))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 90, 50), (10, 255, 255))
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
    mask = cv2.inRange(hsv, (0, 0, 0), (40, 255, 255))
    # mask = cv2.inRange(hsv, (0, 60, 50), (200, 255, 255))
    # mask = cv2.bitwise_not(mask)
    target = cv2.bitwise_and(img,img, mask=mask)
    return target,mask


def main(args=None):
    cnv_width=200
    rclpy.init(args=args)
    node = TomatoPublisher()
    while(cap.isOpened()): 
        ret, frame = cap.read()
        new_frame_time = time.time() 
        if ret:
            img_c=frame
            img_c=mask_crop(img_c,pt1,pt2,pt3,pt4)
            img_c=img_c[pts_x[0]:pts_x[-1],pts_y[0]:pts_y[-1],:]
            #img_c=img_c[:,20:-20,:]
            delay=0
            img_d=img_c.copy()
            img_c=img_c[:,delay:,:]
            # print(img.shape)
            img,thresh =mask_neg(img_c)
            #'''
            contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                x,y,w,h = cv2.boundingRect(cnt)
                if(w*h>2000 and w*h<5000):
                    #print(w*h)
                    img_t=img_c[y:y+h,x:x+w,:]
                    x+=delay
                    img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,0,255),3)
                    img_d = cv2.circle(img_d,(x+(w//2),y+(h//2)),0,(255,0,0),5)
                    img_rm=mask_red(img_t)
                    img_om=mask_org(img_t)
                    img_gm=mask_grn(img_t)
                    mask=[np.sum(img_rm == 255),np.sum(img_om == 255),np.sum(img_gm == 255)]
                    if mask.index(max(mask))==0:
                        img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,0,255),4)
                        cx = (y+h)/2
                        cy = (x+w)/2
                        print(cy)
                    elif mask.index(max(mask))==1:
                        img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,165,255),4)
                        cx = (y+h)/2
                        cy = (x+w)/2
                    elif mask.index(max(mask))==2:
                        img_d = cv2.rectangle(img_d,(x,y),(x+w,y+h),(0,255,0),4)
                        cx = (y+h)/2
                        cy = (x+w)/2
                    if cy>150 and cy<160:
                        #node.publish_tomato_info(mask.index(max(mask)) + 1, cx/img_c.shape[1]*cnv_width)
                        f=open("x.txt",'a')
                        f.write(str(cx/img_c.shape[1]*cnv_width)+' ')
                        f.close()
                        time.sleep(1)
            #img =mask_red(img_c)
            #'''
            #img_rm=mask_red(img)
            #img_om=mask_org(img)
            #img_gm=mask_grn(img)

            #cv2.imshow('o_frame',img_c) 
            cv2.imshow('frame1', img_d) 
            #cv2.imshow('frame', img) 

            #cv2.imshow('red',img_rm) 
            #cv2.imshow('org',img_om) 
            #cv2.imshow('grn',img_gm)
            
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release() 
    cv2.destroyAllWindows() 
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()

