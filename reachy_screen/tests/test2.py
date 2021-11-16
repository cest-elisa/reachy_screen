from reachy_sdk import ReachySDK, joint
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import numpy as np


reachy = ReachySDK(host='127.0.0.1') 

REST_COORD = np.array([
  [-0.17103305,  0.31634818, -0.93309781,  0.33488534],
  [-0.98353147, -0.1109781,   0.14265242, -0.29761366],
  [-0.05842559,  0.94212934,  0.33011931, -0.40],
  [ 0,          0,         0,          1,        ]
])

MID_POS = np.array([
  [ 0, 0, -1,  0.35],
  [ 0, 1, 0, -0.2],
  [ 1, 0, 0, -0.2],
  [ 0, 0, 0, 1]
])

TEST_POS = np.array([
  [0, 0, -1, 0.45],
  [0, 1, 0, 0],
  [1, 0, 0, -0.33],
  [ 0, 0, 0, 1]
])

def joint_goto(goal_coord):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_coord))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )

def joint_goto_2(goal, z):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(np.array([[0, 0, -1, goal[0]],[0, 1, 0, goal[1]],[1, 0, 0, z], [0, 0, 0, 1]])))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )



def main(args=None):
  reachy.turn_on('reachy')
  print("start")
  joint_goto(REST_COORD)
  joint_goto(MID_POS)
  joint_goto(TEST_POS)
  joint_goto(MID_POS)
  joint_goto(TEST_POS)
  joint_goto(MID_POS)
  joint_goto(TEST_POS)
  joint_goto(MID_POS)
  joint_goto(TEST_POS)
  joint_goto(MID_POS)
  joint_goto(REST_COORD)
  reachy.turn_off_smoothly('reachy')
  print("done")
if __name__ == '__main__':
  main()