#!/usr/bin/env python3

# Runs the application.
#   rosrun screen_app run_app.py
#

import rclpy

from screen_app import show_app


def run():
    # Initialise the scenario's ROS node.
    #rospy.init_node('screen_app', anonymous=False)
    rclpy.init(args=sys.argv)
    node = rclpy.create_node('screen_app', anonymous=False)


    node.get_logger().info("Starting a screen application node...")

    # Initialise the human/app window.
    show_app(node)

    # rospy.spin()


if __name__ == '__main__':
    run()
