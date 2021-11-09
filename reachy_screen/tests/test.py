from reachy_sdk import ReachySDK, joint
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np

#TODO : all the links with reachy (--> figure how to get position by pressing a key) 
#TODO : all the links with the screen subscriber
#TODO later : make  the head look at the head ? 
#TODO later : check the temperatures all along to avoid frying some motors
#TODO later : choose which arm moves depending on the distance from goal
#TODO later : choose if otis hand moves or the arm moves depending on distance from goal


reachy = ReachySDK(host='127.0.0.1') 

goal = np.array([0.15, -0.15]) 

REST_COORD = np.array([
  [1, 0, 0, 0.1],
  [0, 1, 0, -0.1],  
  [0, 0, 1, -0.2],
  [0, 0, 0, 1],  
])
matrix_goal = np.array([
            [0., 0., -1., goal[0]],
            [0., 1., 0., goal[1]],
            [1., 0., 0., -0.2], 
            [0, 0, 0, 1]
        ])

"""
funtion to get the new data from the screen subscriber
@param x, y : pixel coordinates of the last pressed position on the screen
"""
def new_coordinates(x, y): 
  new_x = x
  new_y = y
  new_coordinates = True
  print("x = ", x, "; y = ", y, "; new_coord = ", new_coordinates)


"""
"custom" goto function with added inverse kinematics to avoid rewriting the same code over and over
@param goal_coord : array with the x and y goal coordinates in reachy's coordinates
"""
def joint_goto(goal_coord):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_coord))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )



def main(args=None):
  #turn off to ensure compliancy before calibration
    reachy.turn_on('r_arm')
    joint_goto(REST_COORD)
    time.sleep(1.0)
    joint_goto(matrix_goal)
    reachy.turn_off_smoothly('reachy')


if __name__ == '__main__':
    main()