#!/usr/bin/env python3

from numpy import positive
import rclpy # Import the ROS client library for Python
from rclpy.node import Node # Enables the use of rclpy's Node class
import screen_app.msg
import sys
from pynput.keyboard import Key, Listener
#sys.path.append('/.../reachy_screen/touchscreen_ws/src/reachy_touchscreen/screen_touch.py')
#from new_screen import screen_info

class ScreenSubscriber(Node):
  def __init__(self):
    super().__init__('screen_subscriber')
    self.get_logger().info('Ready ros_ws in git !')

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
 

  def listener_callback(self, msg, screen):
        self.get_logger().info('Mouse is at position: x: "{}", y: "{}"'.format(msg.x, msg.y))
        #if (enter) --> get point
        self.position_log.append(msg.x, msg.y)
        print(self.position_log)
        # screen_touch.new_coordinates(msg.x, msg.y)


def on_press(key):
    print('{0} pressed'.format(
        key))
    #if (key == Key.enter):
     # screen_getpoints() #TODO import

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()

def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create the node
  screen_sub = ScreenSubscriber()
  #myScreen = screen_info.Screen()
 
  # Spin the node so the callback function is called.
  # Pull messages from any topics this node is subscribed to.
  rclpy.spin(screen_sub)
 
  # Destroy the node explicitly
  screen_sub.destroy_node()
 
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()

