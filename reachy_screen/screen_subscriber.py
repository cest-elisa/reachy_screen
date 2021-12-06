#!/usr/bin/env python3
from numpy import positive
import rclpy # Import the ROS client library for Python
from rclpy.node import Node # Enables the use of rclpy's Node class
import screen_app.msg
from reachy_sdk import ReachySDK
from screen import screen_info
from screen import screen_getpoints
from screen import screen_touch
import sys

class ScreenSubscriber(Node):
  def __init__(self): 
    super().__init__('screen_subscriber')
    self.get_logger().info('Ready ros_ws in screen_app, not reachy_screen!')
    
    self.my_screen = screen_info.Screen()
    self.my_screen.reachy = ReachySDK(host='127.0.0.1')
    self.my_screen.rest_pos = self.my_screen.reachy.r_arm.forward_kinematics()


    self.position_log = []

    # Create subscriber(s)    
    
    # The node subscribes to messages of type screen_app.msg.Mouse, over a topic named:
    #   /mouse_press
    # The callback function is called as soon as a message is received.
    # The maximum number of queued messages is 10.
    self.subscription_1 = self.create_subscription(
      screen_app.msg.Mouse, 
      '/screen_app/mouse_press', 
      self.listener_callback,
      10)
    self.subscription_1  # prevent unused variable warning


  def listener_callback(self, msg): 
        self.my_screen.reachy.turn_off_smoothly('reachy')
        self.get_logger().info('Mouse is at position: x: "{}", y: "{}"'.format(msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x))
        self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])
        print(self.position_log)
        if(self.my_screen.calibrated == False): 
          screen_getpoints.get_calibration_points(self.my_screen, self.position_log)
        else : 
          screen_touch.screen_touch(self.my_screen, [[0, 0], [self.my_screen.SIZE_SCREEN_X_PX, 0], [0, self.my_screen.SIZE_SCREEN_Y_PX]])



def main(args=None):

  # Initialize the rclpy library
  rclpy.init(args=args)

  # Create the node
  screen_sub = ScreenSubscriber()

  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  rclpy.spin(screen_sub)
 
  # Destroy the node explicitly
  screen_sub.destroy_node()
 
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()