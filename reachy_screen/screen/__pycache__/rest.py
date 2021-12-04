from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import numpy as np


reachy =  ReachySDK(host='127.0.0.1') 


def joint_goto_1(reachy, goal, z):
    goto(
        {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(np.array([[0, 0, -1, goal[0]],
                                                                                                                [0, 1, 0, goal[1]],
                                                                                                                [1, 0, 0, z], 
                                                                                                                [0, 0, 0, 1]])))},
        duration=2.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

right_angled_position = {
    reachy.r_arm.r_shoulder_pitch: 0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: -90,
    reachy.r_arm.r_forearm_yaw: 0,
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll: 0,
}


#reachy.turn_on('reachy')
#joint_goto_1(reachy, [0, -0.2], 0)
print(reachy.r_arm.forward_kinematics())
reachy.turn_off_smoothly('reachy')