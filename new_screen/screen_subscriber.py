#!/usr/bin/env python3

import rclpy # Import the ROS client library for Python
from rclpy.node import Node # Enables the use of rclpy's Node class
import screen_app.msg
import sys
sys.path.append('/.../reachy_screen/touchscreen_ws/src/reachy_touchscreen/screen_touch.py')
import screen_touch
import new_screen

class ScreenSubscriber(Node):
  def __init__(self):
    super().__init__('screen_subscriber')
    self.get_logger().info('Ready ros_ws in git !')
     
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
 

  def listener_callback(self, msg, screen):
        self.get_logger().info('Mouse is at position: x: "{}", y: "{}"'.format(msg.x, msg.y))
        screen_touch.new_coordinates(msg.x, msg.y)

def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create the node
  screen_sub = ScreenSubscriber()
  myScreen = new_screen.screen_info.Screen()
 
  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  rclpy.spin(screen_sub)
 
  # Destroy the node explicitly
  screen_sub.destroy_node()
 
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()
