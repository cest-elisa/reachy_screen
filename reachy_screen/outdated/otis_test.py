from reachy_sdk import ReachySDK
from reachy import Reachy, parts
import sys
import otis
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np


reachy = ReachySDK(host='127.0.0.1')

otis.register()


r = Reachy(
    right_arm=parts.RightArm(io=port, hand='otis')
)

otis = r.right_arm.hand
otis.compliant = False

otis.goto(
        goal_positions={
            'motor_a': 30, 
            'motor_b': 20
        }, 
        duration=0.5,
        wait=True,
    )
otis.drop()

time.sleep(0.5)

a, b, = otis.inverse(0.1, 0.2)
otis.motor_a.goal_position = a
otis.motor_b.goal_position = b
time.sleep(0.025)
    