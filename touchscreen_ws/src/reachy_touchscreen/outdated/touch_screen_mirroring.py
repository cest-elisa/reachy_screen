from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np


reachy = ReachySDK(host='127.0.0.1')


goal_x = 0.4
goal_y = -0.0
fixed_z = -0.25
rest_x = 0.1
rest_y = -0.13
rest_z = -0.1
curr_x, curr_y, curr_z = reachy.r_arm.forward_kinematics()[:3, -1]
print(fixed_z)
print(curr_x, curr_y, curr_z)



A = np.array([
  [0, 0, -1, goal_x],
  [0, 1, 0, goal_y],  
  [1, 0, 0, fixed_z],
  [0, 0, 0, 1],  
])

B = np.array([
  [0, 0, -1, goal_x],
  [0, 1, 0, goal_y],  
  [1, 0, 0, fixed_z + 0.2],
  [0, 0, 0, 1],  
])

C = np.array([
  [0, 0, -1, curr_x],
  [0, 1, 0, curr_y],  
  [1, 0, 0, curr_z + 0.1],
  [0, 0, 0, 1],  
])

R = np.array([
  [1, 0, 0, rest_x],
  [0, 1, 0, rest_y],  
  [0, 0, 1, rest_z],
  [0, 0, 0, 1],  
])

joint_pos_A = reachy.r_arm.inverse_kinematics(A)
joint_pos_B = reachy.r_arm.inverse_kinematics(B)
joint_pos_C = reachy.r_arm.inverse_kinematics(C)
joint_pos_R = reachy.r_arm.inverse_kinematics(R)

reachy.turn_on('reachy')

goto(
            {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_C)},
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

goto(
            {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_B)},
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

goto(
            {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_A)}, 
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    
time.sleep(2.0)

goto(
            {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_B)},
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

goto(
            {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_R)},
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

time.sleep(2.0)

reachy.turn_off_smoothly('reachy')

