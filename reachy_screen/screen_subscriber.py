#!/usr/bin/env python3

import rclpy # Import the ROS client library for Python
from rclpy.node import Node # Enables the use of rclpy's Node class
import screen_app.msg
import justhink_interfaces.msg
from reachy_sdk import ReachySDK
from screen import screen_info
from screen import screen_getpoints
from screen import screen_touch

MEAN_ERR_PX = 90

"""
  scren subscriber node to listen when and where the screen has been pressed
"""
class ScreenSubscriber(Node):
  def __init__(self): 
    super().__init__('screen_subscriber')
    self.get_logger().info('Ready ros_ws in screen_app, not reachy_screen!')
    
    self.my_screen = screen_info.Screen()
    self.my_screen.reachy = ReachySDK(host='127.0.0.1')
    self.my_screen.reachy.turn_off_smoothly('reachy')
    self.my_screen.rest_pos = self.my_screen.reachy.r_arm.forward_kinematics()
    self.my_screen.rest_pos[2, 3] += 0.02
    print("")
    print(self.my_screen.rest_pos)
    print("")


    self.position_log = []

    # Create subscriber(s)    
    
    # The node subscribes to messages of type screen_app.msg.Mouse, over a topic named:
    #   /mouse_press
    # The callback function is called as soon as a message is received.
    # The maximum number of queued messages is 10.
    self.subscription_1 = self.create_subscription(
      screen_app.msg.Mouse, 
      '/screen_app/mouse_press', 
      self.touchscreen_sub,
      10)
    self.subscription_1  # prevent unused variable warning
    '''
    '''
    self.subscription_2 = self.create_subscription(
      justhink_interfaces.msg.PointDrawing,
      '/justhink_touch/intended_points',
      self.gametouch_sub,
      10)
    self.subscription_2 

  def touchscreen_sub(self, msg): 
        self.my_screen.reachy.turn_off_smoothly('reachy')

        print(" - - - - - new touch recorded - - - - -")
        self.get_logger().info('Real mouse position: x: "{}", y: "{}"'.format(msg.x, msg.y))
        self.get_logger().info('Arranged mouse position: x: "{}", y: "{}"'.format(msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x))
        #self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])
        print(self.position_log)

        if(self.my_screen.calibrated == False): 
          self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])
          screen_getpoints.get_calibration_points(self.my_screen, self.position_log)
        
        elif(self.my_screen.calib_step < 40 ):
          self.my_screen.calib_step += 11
          last_log = self.position_log[-1:]
          print(last_log)
          print(last_log[0][0] - msg.y + last_log[0][1] - self.my_screen.SIZE_SCREEN_Y_PX + msg.x )
          if(abs(last_log[0][0] - msg.y + last_log[0][1] - self.my_screen.SIZE_SCREEN_Y_PX + msg.x ) > 400):
            screen_touch.screen_touch(self.my_screen, [[msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x]])
            self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])


        else : 
          self.my_screen.calib_step += 1
          self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])
          print(self.position_log)
          print(" - nada - ")

        """
        # TESTING IF IT FOLLOWS WHERE I TOUCH
        else :
          last_pos = self.position_log[-1:][0]
          print("my if condition > 200 : ", abs(last_pos[0] + last_pos[1] - msg.y - self.my_screen.SIZE_SCREEN_Y_PX + msg.x))
          if(abs(last_pos[0] + last_pos[1] - msg.y - self.my_screen.SIZE_SCREEN_Y_PX + msg.x) > 200):
            self.position_log.append([msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x])
            print(self.position_log)

            if(self.my_screen.calib_step < 20 and self.my_screen.calib_step%2 == 0):
              screen_touch.screen_touch(self.my_screen, [[msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x]])
              self.my_screen.calib_step += 1

            else :
              #screen_touch.screen_touch(self.my_screen, [[msg.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.x]])
              self.my_screen.calib_step += 1
              print("")
              print(" - - - skipped touch - - - ")
              print("")
          """


  
  def gametouch_sub(self, msg):
    self.my_screen.reachy.turn_off_smoothly('reachy')
    self.get_logger().info('Game touch points - from : "{}", to : "{}"'.format(msg.from_point, msg.to_point))
    print("- - - - new point - - - - ")
    self.position_log.append([[msg.from_point.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.from_point.x], 
                              [msg.to_point.y  , self.my_screen.SIZE_SCREEN_Y_PX - msg.to_point.x  ]])
    print(self.position_log)

    screen_touch.screen_touch(self.my_screen, [[msg.from_point.y, self.my_screen.SIZE_SCREEN_Y_PX - msg.from_point.x], 
                                               [msg.to_point.y  , self.my_screen.SIZE_SCREEN_Y_PX - msg.to_point.x  ]])
    print()





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