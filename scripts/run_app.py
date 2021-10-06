#!/usr/bin/env python3

# Runs the application.
#   rosrun screen_app run_app.py
#

import rospy

from screen_app import show_app


def run():
    # Initialise the scenario's ROS node.
    rospy.init_node('screen_app', anonymous=False)

    rospy.loginfo("Starting a screen application node...")

    # Initialise the human/app window.
    show_app()

    rospy.spin()


if __name__ == '__main__':
    run()
