from reachy_sdk import ReachySDK
import time

reachy = ReachySDK(host='127.0.0.1')


reachy.turn_on('head')
reachy.turn_off_smoothly('reachy')

import time

look_right = reachy.head.look_at(x=0.5, y=-0.5, z=0.1, duration=1.0)
time.sleep(0.1)
look_down = reachy.head.look_at(x=0.5, y=0, z=-0.4, duration=1.0)
time.sleep(0.1)
look_left = reachy.head.look_at(x=0.5, y=0.3, z=-0.3, duration=1.0)
time.sleep(0.1)
look_front = reachy.head.look_at(x=0.5, y=0, z=0, duration=1.0)


x, y, z = reachy.r_arm.forward_kinematics()[:3,-1] # We want the translation part of Reachy's pose matrix
reachy.head.look_at(x=x, y=y, z=z-0.05, duration=1.0) # There is a 5cm offset on the z axis

time.sleep(0.5)

while True:
    x, y, z = reachy.r_arm.forward_kinematics()[:3,-1]
    gp_dic = reachy.head._look_at(x, y, z - 0.05)
    reachy.head.neck_disk_bottom.goal_position = gp_dic[reachy.head.neck_disk_bottom]
    reachy.head.neck_disk_middle.goal_position = gp_dic[reachy.head.neck_disk_middle]
    reachy.head.neck_disk_top.goal_position = gp_dic[reachy.head.neck_disk_top]
    time.sleep(0.01)
