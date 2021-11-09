from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time

reachy = ReachySDK(host='127.0.0.1')


##positions : 

sheeesh = {
    reachy.r_arm.r_shoulder_pitch: -41.12,
    reachy.r_arm.r_shoulder_roll: -11.14,
    reachy.r_arm.r_arm_yaw: 26.68,
    reachy.r_arm.r_elbow_pitch: -14.02,
    reachy.r_arm.r_forearm_yaw: -24.49,
    reachy.r_arm.r_wrist_pitch: -9.54,
    reachy.r_arm.r_wrist_roll: -28.01,
    reachy.l_arm.l_shoulder_pitch: -18.97,
    reachy.l_arm.l_shoulder_roll: -14.88,
    reachy.l_arm.l_arm_yaw: -61.49,
    reachy.l_arm.l_elbow_pitch: -57.1,
    reachy.l_arm.l_forearm_yaw: -52.64,
    reachy.l_arm.l_wrist_pitch: -32.31,
    reachy.l_arm.l_wrist_roll: -15.98,
}

stoos = {
    reachy.r_arm.r_shoulder_pitch: 2.75,
    reachy.r_arm.r_shoulder_roll: -66.35,
    reachy.r_arm.r_arm_yaw: 74.86,
    reachy.r_arm.r_elbow_pitch: -93.49,
    reachy.r_arm.r_forearm_yaw: -60.85,
    reachy.r_arm.r_wrist_pitch: -14.02,
    reachy.r_arm.r_wrist_roll: -8.94,
    reachy.l_arm.l_shoulder_pitch: 22.88,
    reachy.l_arm.l_shoulder_roll: 69.6,
    reachy.l_arm.l_arm_yaw: -48.84,
    reachy.l_arm.l_elbow_pitch: -85.76,
    reachy.l_arm.l_forearm_yaw: -39.44,
    reachy.l_arm.l_wrist_pitch: -54.99,
    reachy.l_arm.l_wrist_roll: 4.84,
}

right_angled = {
    reachy.r_arm.r_shoulder_pitch: 0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: -90,
    reachy.r_arm.r_forearm_yaw: 0,
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll: 0,
    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 0,
    reachy.l_arm.l_arm_yaw: 0,
    reachy.l_arm.l_elbow_pitch: -90,
    reachy.l_arm.l_forearm_yaw: 0,
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll: 0,
}


reachy.turn_on('reachy')

goto(
	goal_positions=right_angled,
	duration=2.0,
	interpolation_mode=InterpolationMode.MINIMUM_JERK
	)

time.sleep(0.1)

goto(
	goal_positions=sheeesh,
	duration=2.0,
	interpolation_mode=InterpolationMode.MINIMUM_JERK
	)

time.sleep(0.1)

goto(
	goal_positions=stoos,
	duration=2.0,
	interpolation_mode=InterpolationMode.MINIMUM_JERK
	)

time.sleep(0.1)

goto(
	goal_positions=right_angled,
	duration=2.0,
	interpolation_mode=InterpolationMode.MINIMUM_JERK
	)

time.sleep(0.1)

reachy.turn_off_smoothly('reachy')
