from reachy_sdk import ReachySDK
import reachy_sdk
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np
import screen_processing

reachy = ReachySDK(host='127.0.0.1')

REST_COORD = np.array([
  [1, 0, 0, 0.1],
  [0, 1, 0, -0.1],  
  [0, 0, 1, -0.1],
  [0, 0, 0, 1],  
])


# just to avoid rewriting the same code over and over
def joint_goto(goal_coord):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_coord))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )

def look_at_hand(goal_coord):
  x, y, z = goal_coord[:3,-1] # We want the translation part of Reachy's pose matrix
  print("x,y,z = ", x, y, z)
  reachy.head.look_at(x=x, y=y, z=z-0.05, duration=1.0) # There is a 5cm offset on the z axis

  time.sleep(0.5)
  x, y, z = goal_coord[:3,-1]
  gp_dic = reachy.head._look_at(x, y, z - 0.05)
  reachy.head.neck_disk_bottom.goal_position = gp_dic[reachy.head.neck_disk_bottom]
  reachy.head.neck_disk_middle.goal_position = gp_dic[reachy.head.neck_disk_middle]
  reachy.head.neck_disk_top.goal_position = gp_dic[reachy.head.neck_disk_top]
  time.sleep(0.01)



def main(args=None):
  #reachy.turn_on('reachy')
  #joint_goto(REST_COORD)
  goal_coords = screen_processing.rescale_destination(150, 500)
  print(goal_coords)
  #look_at_hand(goal_coords)
  #joint_goto(goal_coords)
  #time.sleep(1.0)
  #joint_goto(REST_COORD)
  reachy.turn_off_smoothly('reachy')

if __name__ == '__main__':
    main()