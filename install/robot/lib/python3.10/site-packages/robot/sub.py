import os
import rclpy
from rclpy.node import Node
from custom_messages.msg import Posvel
#from example_interfaces.srv import GetPosition
from dynamixel_sdk import *

class ReadWritePyNode(Node):
    def __init__(self):
        super().__init__('read_write_py_node')
        self.portHandler = PortHandler('/dev/ttyUSB0')
        self.packetHandler = PacketHandler(2.0)

        self.subscription = self.create_subscription(
            Posvel,
            'set_position_n',
            self.set_goal_pos_callback,
            10
        )

    def set_goal_pos_callback(self, msg):
        self.get_logger().info(f"Set Goal Position of ID = {msg.position1}")

def main(args=None):
    rclpy.init(args=args)
    read_write_py_node = ReadWritePyNode()

    try:
        read_write_py_node.portHandler.openPort()
        read_write_py_node.get_logger().info('Succeeded to open the port')
    except:
        read_write_py_node.get_logger().info('Failed to open the port')
        read_write_py_node.get_logger().info('Press any key to terminate...')
        
        quit()

    try:
        read_write_py_node.portHandler.setBaudRate(115200)
        read_write_py_node.get_logger().info('Succeeded to change the baudrate')
    except:
        read_write_py_node.get_logger().info('Failed to change the baudrate')
        read_write_py_node.get_logger().info('Press any key to terminate...')
       
        quit()

    dxl_comm_result, dxl_error = read_write_py_node.packetHandler.write1ByteTxRx(read_write_py_node.portHandler, 1, 64, 1)
    if dxl_comm_result != 0:
        read_write_py_node.get_logger().info(f"{read_write_py_node.packetHandler.getTxRxResult(dxl_comm_result)}")
        read_write_py_node.get_logger().info('Press any key to terminate...')
        
        quit()
    elif dxl_error != 0:
        read_write_py_node.get_logger().info(f"{read_write_py_node.packetHandler.getRxPacketError(dxl_error)}")
        read_write_py_node.get_logger().info('Press any key to terminate...')
         	
        quit()
    else:
        read_write_py_node.get_logger().info('DYNAMIXEL has been successfully connected')

    read_write_py_node.get_logger().info('Ready to get & set Position.')

    rclpy.spin(read_write_py_node)
    read_write_py_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
