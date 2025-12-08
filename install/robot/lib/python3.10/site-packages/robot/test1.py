import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel
from robot.ik import *
import curses
import numpy as np 
import cv2 
import time 

x, y, z, al1, al2, al3 = 250,0,350,-90,0,0

class SetPositionPublisher(Node):

    def __init__(self):
        super().__init__('set_position_publisher_n')
        self.publisher = self.create_publisher(Posvel, '/set_position_n', 10)
        self.position_msg = Posvel()
        self.rate = self.create_rate(10)
        rad = 3.14159265359/180
        
                    
        while True:
             
                input_str = input("Enter the x, y, z, al1, al2, al3 values (space-separated) or 'exit' to quit -> ")
                print(str)
                if input_str.lower() == 'exit':
                    break

                numbers = list(map(float, input_str.split()))

                if len(numbers) != 6:
                    print("Invalid input, please enter 6 numbers.")
                    continue
  
                
                global z,al1,al2,al3
                print("The x, y, z -> ",x,y,z)
                q1, q2, q3, q4, q5, q6 = fcn(x,y,z,al1,al2,al3) #0, 0, 0, 0, 0, 0  # Simulated values
                #q1, q2, q3, q4, q5, q6 = 0, 0, 0, 0, 0, 0
                print("The x, y, z -> ",x,y,z)
                
                #print(f"{round(q1 / rad)} {round(q2 / rad)} {round(q3 / rad)} {round(q4 / rad)} {round(q5 / rad)} {round(q6 / rad)}")

                #self.position_msg.position1 = x #float(round(q1 / self.rad))
                #self.position_msg.position2 = y #float(round(q2 / self.rad))
                #self.position_msg.position3 = z #float(round(q3 / self.rad))
                #self.position_msg.position4 = al1 #float(round(q4 / self.rad))
                #self.position_msg.position5 = al2 #float(round(q5 / self.rad))
                #self.position_msg.position6 = al3 #float(round(q6 / self.rad))
                
                self.position_msg.position1 = float((q1 / rad))
                self.position_msg.position2 = float((q2 / rad))
                self.position_msg.position3 = float((q3 / rad))
                self.position_msg.position4 = float((q4 / rad))
                self.position_msg.position5 = float((q5 / rad))
                self.position_msg.position6 = float((q6 / rad))

                self.publisher.publish(self.position_msg)
                #self.get_logger().info(f"Published SetPosition message: position1={self.position_msg.position1}, "
                 #                      f"position2={self.position_msg.position2}, position3={self.position_msg.position3}, "
                  #                     f"position4={self.position_msg.position4}, position5={self.position_msg.position5}, "
                   #                    f"position6={self.position_msg.position6}")
                #print(self.position_msg.position1,self.position_msg.position2,self.position_msg.position3)
                 
        
        self.get_logger().info("Exiting...")

def main(args=None):
    rclpy.init(args=args)
    set_position_publisher = SetPositionPublisher()
    rclpy.spin(set_position_publisher)
    set_position_publisher.destroy_node()
    rclpy.shutdown()
'''
def main(stdscr, args=None):  # Pass stdscr as an argument
    rclpy.init(args=args)
    set_position_publisher = SetPositionPublisher(stdscr)
    rclpy.spin(set_position_publisher)
    set_position_publisher.destroy_node()
    rclpy.shutdown()
'''
if __name__ == '__main__':
    #curses.wrapper(main)
    main()

