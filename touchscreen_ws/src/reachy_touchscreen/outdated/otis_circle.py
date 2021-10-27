import numpy as np
from matplotlib import pyplot as plt
import otis

otis.register()

import sys

if sys.platform == 'linux':
    port = '/dev/ttyUSB*'
elif sys.platform == 'darwin':
    port = '/dev/cu.usb*'
else:
    # port = 'COMX'
    raise EnvironmentError('Please set the correct number for the COM port')

from reachy import Reachy, parts

r = Reachy(
    right_arm=parts.RightArm(io=port, hand='otis')
)

otis = r.right_arm.hand
center = (78, 112)
radius = 10
import time

otis.compliant = False

otis.lift()

theta = np.linspace(0, 2 * np.pi, 1000)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

theta_a, theta_b = otis.inverse(x, y)

otis.goto(
    goal_positions={
        'motor_a': theta_a[0], 
        'motor_b': theta_b[0]
    }, 
    duration=0.5,
)

otis.drop()

for a, b in zip(theta_a, theta_b):
    otis.motor_a.goal_position = a
    otis.motor_b.goal_position = b
    time.sleep(0.01)
    
otis.lift()