import tkinter as tk
from tkinter import messagebox
import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel, mode
from robot.ik import fcn
import threading

class SetPositionPublisher(Node):

    def __init__(self):
        super().__init__('set_position_publisher_n')
        self.publisher = self.create_publisher(Posvel, '/set_position_n', 10)
        self.position_msg = Posvel()
        self.rad = 3.14159265359 / 180
        
	
        self.root = tk.Tk()
        self.root.title("Robot Arm Controller")
        self.root.geometry("1000x600")
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
	
        self.label_x = tk.Label(self.root, text="X:")
        self.label_x.place(x = sw*0.28,y=sh*0.38)
        self.entry_x = tk.Entry(self.root)
        self.entry_x.place(x = sw*0.3,y=sh*0.38)

        self.label_y = tk.Label(self.root, text="Y:")
        self.label_y.place(x = sw*0.28,y=sh*0.42)
        self.entry_y = tk.Entry(self.root)
        self.entry_y.place(x = sw*0.3,y=sh*0.42)

        self.label_z = tk.Label(self.root, text="Z:")
        self.label_z.place(x = sw*0.28,y=sh*0.46)
        self.entry_z = tk.Entry(self.root)
        self.entry_z.place(x = sw*0.3,y=sh*0.46)

        self.label_roll = tk.Label(self.root, text="Roll:")
        self.label_roll.place(x = sw*0.4,y=sh*0.38)
        self.entry_roll = tk.Entry(self.root)
        self.entry_roll.place(x = sw*0.43,y=sh*0.38)

        self.label_pitch = tk.Label(self.root, text="Pitch:")
        self.label_pitch.place(x = sw*0.4,y=sh*0.42)
        self.entry_pitch = tk.Entry(self.root)
        self.entry_pitch.place(x = sw*0.43,y=sh*0.42)

        self.label_yaw = tk.Label(self.root, text="Yaw:")
        self.label_yaw.place(x = sw*0.4,y=sh*0.46)
        self.entry_yaw = tk.Entry(self.root)
        self.entry_yaw.place(x = sw*0.43,y=sh*0.46)
        
        ############################################
        
        self.label_x1 = tk.Label(self.root, text="Q1:")
        self.label_x1.place(x = sw*0.02,y=sh*0.38)
        self.entry_x1 = tk.Entry(self.root)
        self.entry_x1.place(x = sw*0.04,y=sh*0.38)

        self.label_y1 = tk.Label(self.root, text="Q2:")
        self.label_y1.place(x = sw*0.02,y=sh*0.42)
        self.entry_y1 = tk.Entry(self.root)
        self.entry_y1.place(x = sw*0.04,y=sh*0.42)

        self.label_z1 = tk.Label(self.root, text="Q3:")
        self.label_z1.place(x = sw*0.02,y=sh*0.46)
        self.entry_z1 = tk.Entry(self.root)
        self.entry_z1.place(x = sw*0.04,y=sh*0.46)

        self.label_roll1 = tk.Label(self.root, text="Q4:")
        self.label_roll1.place(x = sw*0.13,y=sh*0.38)
        self.entry_roll1 = tk.Entry(self.root)
        self.entry_roll1.place(x = sw*0.15,y=sh*0.38)

        self.label_pitch1 = tk.Label(self.root, text="Q5:")
        self.label_pitch1.place(x = sw*0.13,y=sh*0.42)
        self.entry_pitch1 = tk.Entry(self.root)
        self.entry_pitch1.place(x = sw*0.15,y=sh*0.42)

        self.label_yaw1 = tk.Label(self.root, text="Q6:")
        self.label_yaw1.place(x = sw*0.13,y=sh*0.46)
        self.entry_yaw1 = tk.Entry(self.root)
        self.entry_yaw1.place(x = sw*0.15,y=sh*0.46)
       
            
        self.button = tk.Button(self.root, text="Ikine", command=self.publish_message,width = 8,height=1)
        self.button.place(x = sw*0.37,y=sh*0.5)
        
        self.title = tk.Label(self.root, text="Inverse Kinematics")
        self.title.place(x = sw*0.37,y=sh*0.33)
        
        self.button1 = tk.Button(self.root, text="Fkine", command=self.publish_message1,width = 8,height=1)
        self.button1.place(x = sw*0.12,y=sh*0.5)
        
        self.on = tk.Button(self.root, text="ON", command=self.on,width = 8,height=1)
        self.on.place(x = sw*0.05,y=sh*0.05)
        
        self.off = tk.Button(self.root, text="OFF", command=self.off,width = 8,height=1)
        self.off.place(x = sw*0.15,y=sh*0.05)
        
        self.title1 = tk.Label(self.root, text="Forward Kinematics")
        self.title1.place(x = sw*0.1,y=sh*0.33)
        
        self.title2 = tk.Label(self.root, text="Torque ")
        self.title2.place(x = sw*0.11,y=sh*0.1)
        
        self.count = 0
        self.red = 0
        self.orng=0
        self.green=0
        
        self.label_count = tk.Label(self.root, text="Total Count:")
        self.label_count.place(x=sw * 0.36, y=sh * 0.03)
        self.label_count_value = tk.Label(self.root, text=str(self.count))
        self.label_count_value.place(x=sw * 0.44, y=sh * 0.03)
        
        self.label_count = tk.Label(self.root, text="Red Tomato")
        self.label_count.place(x=sw * 0.25, y=sh * 0.08)
        self.label_count_value = tk.Label(self.root, text=str(self.red))
        self.label_count_value.place(x=sw * 0.33, y=sh * 0.08)
        
        self.label_count = tk.Label(self.root, text="Orange Tomato")
        self.label_count.place(x=sw * 0.25, y=sh * 0.14)
        self.label_count_value = tk.Label(self.root, text=str(self.red))
        self.label_count_value.place(x=sw * 0.33, y=sh * 0.14)
        
        self.label_count = tk.Label(self.root, text="Green Tomato")
        self.label_count.place(x=sw * 0.25, y=sh * 0.2)
        self.label_count_value = tk.Label(self.root, text=str(self.red))
        self.label_count_value.place(x=sw * 0.33, y=sh * 0.2)
        
        self.home = tk.Button(self.root, text="Home", command=self.home,width = 8,height=1)
        self.home.place(x = sw*0.05,y=sh*0.2)
        self.rest = tk.Button(self.root, text="Rest", command=self.rest,width = 8,height=1)
        self.rest.place(x = sw*0.15,y=sh*0.2)
        
        
    def home(self):
        self.position_msg.position1 = 0.0 #float(q1 / self.rad)
        self.position_msg.position2 = 90.0 #float(q2 / self.rad)
        self.position_msg.position3 = 0.0 #float(q3 / self.rad)
        self.position_msg.position4 = 0.0 #float(q4 / self.rad)
        self.position_msg.position5 = 0.0 #float(q5 / self.rad)
        self.position_msg.position6 = 0.0
        
        self.pub(self.position_msg)
        
    def rest(self):
        self.position_msg.position1 = 0.0 #float(q1 / self.rad)
        self.position_msg.position2 = 40.0 #float(q2 / self.rad)
        self.position_msg.position3 = 119.0 #float(q3 / self.rad)
        self.position_msg.position4 = 0.0 #float(q4 / self.rad)
        self.position_msg.position5 = -90.0 #float(q5 / self.rad)
        self.position_msg.position6 = 0.0
        
        self.pub(self.position_msg)
        

    def on(self):
    	self.position_msg.torque=1
    	self.position_msg.position1 = float(-1.234)
    	self.publisher.publish(self.position_msg)
    	self.get_logger().info(f"Published SetPosition message: torque={self.position_msg.torque}")

    def off(self):
    	self.position_msg.torque=0
    	self.position_msg.position1 = float(-1.234)
    	self.publisher.publish(self.position_msg)
    	self.get_logger().info(f"Published SetPosition message: torque={self.position_msg.torque}")
    	
    def publish_message(self):
        try:
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            z = float(self.entry_z.get())
            roll = float(self.entry_roll.get())
            pitch = float(self.entry_pitch.get())
            yaw = float(self.entry_yaw.get())

            q1, q2, q3, q4, q5, q6 = fcn(x, y, z, roll, pitch, yaw)
            print(q1,q2,q3)
            self.position_msg.position1 = float(q1 / self.rad)
            self.position_msg.position2 = float(q2 / self.rad)
            self.position_msg.position3 = float(q3 / self.rad)
            self.position_msg.position4 = float(q4 / self.rad)
            self.position_msg.position5 = float(q5 / self.rad)
            self.position_msg.position6 = float(q6 / self.rad)
            
            self.pub(self.position_msg)
	
	 
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input format: {e}")
            
    def publish_message1(self):
        try:
            x = float(self.entry_x1.get())
            y = float(self.entry_y1.get())
            z = float(self.entry_z1.get())
            roll = float(self.entry_roll1.get())
            pitch = float(self.entry_pitch1.get())
            yaw = float(self.entry_yaw1.get())

            q1, q2, q3, q4, q5, q6 = x, y, z, roll, pitch, yaw

            self.position_msg.position1 = float(q1)
            self.position_msg.position2 = float(q2)
            self.position_msg.position3 = float(q3)
            self.position_msg.position4 = float(q4)
            self.position_msg.position5 = float(q5)
            self.position_msg.position6 = float(q6)

            self.pub(self.position_msg)

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input format: {e}")
            
    def pub(self,position_msg):
        print(self.position_msg.position1,self.position_msg.position2,self.position_msg.position3)
		
        self.publisher.publish(self.position_msg)
        self.get_logger().info(f"Published SetPosition message: position1={self.position_msg.position1}, "
                               f"position2={self.position_msg.position2}, position3={self.position_msg.position3}, "
                               f"position4={self.position_msg.position4}, position5={self.position_msg.position5}, "
                               f"position6={self.position_msg.position6}")
    def spin_gui(self):
        self.root.mainloop()


def main(args=None):
    rclpy.init(args=args)
    set_position_publisher = SetPositionPublisher()
    set_position_publisher.spin_gui()


if __name__ == '__main__':
    main()

