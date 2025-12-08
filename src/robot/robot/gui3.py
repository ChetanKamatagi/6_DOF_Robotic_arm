import tkinter as tk
from tkinter import messagebox
import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel
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
        self.root.geometry("600x600")
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
	
        self.label_x = tk.Label(self.root, text="X:")
        self.label_x.place(x = sw*0.02,y=sh*0.005)
        self.entry_x = tk.Entry(self.root)
        self.entry_x.place(x = sw*0.04,y=sh*0.005)

        self.label_y = tk.Label(self.root, text="Y:")
        self.label_y.place(x = sw*0.02,y=sh*0.04)
        self.entry_y = tk.Entry(self.root)
        self.entry_y.place(x = sw*0.04,y=sh*0.04)

        self.label_z = tk.Label(self.root, text="Z:")
        self.label_z.place(x = sw*0.02,y=sh*0.08)
        self.entry_z = tk.Entry(self.root)
        self.entry_z.place(x = sw*0.04,y=sh*0.08)

        self.label_roll = tk.Label(self.root, text="Roll:")
        self.label_roll.place(x = sw*0.15,y=sh*0.005)
        self.entry_roll = tk.Entry(self.root)
        self.entry_roll.place(x = sw*0.18,y=sh*0.005)

        self.label_pitch = tk.Label(self.root, text="Pitch:")
        self.label_pitch.place(x = sw*0.15,y=sh*0.04)
        self.entry_pitch = tk.Entry(self.root)
        self.entry_pitch.place(x = sw*0.18,y=sh*0.04)

        self.label_yaw = tk.Label(self.root, text="Yaw:")
        self.label_yaw.place(x = sw*0.15,y=sh*0.08)
        self.entry_yaw = tk.Entry(self.root)
        self.entry_yaw.place(x = sw*0.18,y=sh*0.08)
        
        pre_vals = [30,40,50,60,80,99]
        self.sliders = []
        self.slider_labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
        self.slider_vals = [180] * 6
        for i in range(6):
            label = tk.Label(self.root, text=f"{self.slider_labels[i]}:")
            label.place(x=sw*0.05, y=190 + 50 * i)
            slider = tk.Scale(self.root, from_=0, to=360, orient=tk.HORIZONTAL, length=300)
            slider.set(pre_vals[i])
            slider.place(x=sw*0.08, y=170 + 50 * i)
            self.sliders.append(slider)
            self.slider_vals[1] = 90
            
        self.button = tk.Button(self.root, text="Publish", command=self.publish_message,width = 8,height=1)
        self.button.place(x = sw*0.12,y=sh*0.12)
        
        self.timer = threading.Timer(0.5, self.periodic_publish)
        self.timer.start()


    def publish_message(self):
        try:
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            z = float(self.entry_z.get())
            roll = float(self.entry_roll.get())
            pitch = float(self.entry_pitch.get())
            yaw = float(self.entry_yaw.get())

            q1, q2, q3, q4, q5, q6 = fcn(x, y, z, roll, pitch, yaw)

            self.position_msg.position1 = float(q1 / self.rad)
            self.position_msg.position2 = float(q2 / self.rad)
            self.position_msg.position3 = float(q3 / self.rad)
            self.position_msg.position4 = float(q4 / self.rad)
            self.position_msg.position5 = float(q5 / self.rad)
            self.position_msg.position6 = float(q6 / self.rad)

            self.publisher.publish(self.position_msg)
            self.get_logger().info(f"Published SetPosition message: position1={self.position_msg.position1}, "
                                   f"position2={self.position_msg.position2}, position3={self.position_msg.position3}, "
                                   f"position4={self.position_msg.position4}, position5={self.position_msg.position5}, "
                                   f"position6={self.position_msg.position6}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input format: {e}")
            
    def periodic_publish(self):
    	q1, q2, q3, q4, q5, q6 = [val for val in self.slider_vals]
    	for i in range(6):
    		self.slider_vals[i] = self.sliders[i].get()
    		
    	q1, q2, q3, q4, q5, q6 = [val for val in self.slider_vals]
    	self.position_msg.position1 = float(q1 / self.rad)
    	self.position_msg.position2 = float(q2 / self.rad)
    	self.position_msg.position3 = float(q3 / self.rad)
    	self.position_msg.position4 = float(q4 / self.rad)
    	self.position_msg.position5 = float(q5 / self.rad)
    	self.position_msg.position6 = float(q6 / self.rad)
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

