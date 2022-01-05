from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from screen import screen_processing
import numpy as np
import time

# testing : DONE
# works : YES, DO NOT TOUCH !!!


"""
  making reachy touch, in sequence, and array of points, and returning to his resting hand position
  @param screen : all the screen information
  @param dest_coord_array : array of all the points we want to touch written as : [[x_1, y_1], [x_2, y_2], ..., [x_n, y_n]]
"""

def screen_touch(screen, dest_coord_array): 
   
    n = len(dest_coord_array)

    screen.reachy.turn_on('r_arm')

    joint_goto_1(screen.reachy, [screen.rest_pos[0, 3], screen.rest_pos[1, 3]], screen.rest_pos[2, 3] + 0.2)

    
    for i in range(n): 
        next_pos = screen_processing.processing_screen_point(screen, dest_coord_array[i])
        joint_goto_1(screen.reachy, next_pos, screen.fixed_z + 0.2)
        joint_goto_1(screen.reachy, next_pos, screen.fixed_z + 0.02)
        joint_goto_1(screen.reachy, next_pos, screen.fixed_z + 0.2)

    joint_goto_1(screen.reachy, [screen.rest_pos[0, 3], screen.rest_pos[1, 3]], screen.fixed_z + 0.2)
    joint_goto_2(screen.reachy, screen.rest_pos)
    screen.reachy.turn_off_smoothly('reachy')   
    


"""
  making reachy actually touch a point given an array [x, y] with goal position
  @param reachy : reachy
  @param goal : array of the point we want to touch [x_1, y_1] in reachy's coordinate system
  @param z : screen's fixed height, determined through initial calibration
"""
def joint_goto_1(reachy, goal, z):
    goto(
        {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(np.array([[0,   0,  -1, goal[0]],
                                                                                                                 [0,   1,   0, goal[1]],
                                                                                                                 [1,   0,   0,       z], 
                                                                                                                 [0,   0,   0,       1]])))},
        duration=1.5,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )




"""
  making reachy actually touch a point, given a quaternion instead of [x, y] coordinates
  @param reachy : reachy
  @param goal_coords : quaternion of the point we want to reach
"""

def joint_goto_2(reachy, goal_quaternion):
    goto(
        {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_quaternion))},
        duration=1.5,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )