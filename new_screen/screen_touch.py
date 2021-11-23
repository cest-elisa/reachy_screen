
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np
import otis


# TODO : check if we want to press the point, or drag between two point

def screen_touch(reachy, screen, dest_coord_array): 
    n = len(dest_coord_array)
    if (n%2 == 1) :
        print("array has odd number of elements, please try again")
    else :
        reachy.turn_on('r_arm')
        joint_goto_1(reachy, [screen.rest_pos[0, 3], screen.rest_pos[1, 3]], screen.rest_pos[2, 3] + 0.1)

        # for loop to make reachy press all the desired points in the destination array
        for i in range(n) :
            next_pos = [dest_coord_array[2*i], dest_coord_array[2*i + 1]]
            joint_goto_1(reachy, next_pos, screen.fixed_z + 0.2)
            joint_goto_1(reachy, next_pos, screen.fixed_z)
            otis.drop()
            otis.lift()

        joint_goto_2(reachy, screen.rest_pos)
        reachy.turn_off_smoothly('reachy')     


#eventually update with romain's dietics goto
def joint_goto_1(reachy, goal, z):
    goto(
        {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(np.array([[0, 0, -1, goal[0]],
                                                                                                                [0, 1, 0, goal[1]],
                                                                                                                [1, 0, 0, z], 
                                                                                                                [0, 0, 0, 1]])))},
        duration=2.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

def joint_goto_2(reachy, goal_coord):
    goto(
        {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_coord))},
        duration=2.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )