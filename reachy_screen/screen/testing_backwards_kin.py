from reachy_sdk import ReachySDK


reachy = ReachySDK(host='127.0.0.1')
print(reachy.r_arm.forward_kinematics())