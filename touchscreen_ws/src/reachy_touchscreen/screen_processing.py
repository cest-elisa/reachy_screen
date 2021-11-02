import numpy as np
import screen_calibration


# screen size in pixels
SIZE_SCREEN_X_PX = 1080  
SIZE_SCREEN_Y_PX = 1920

#TODO - check if the screen size is the correct one
# screen size in meters
SIZE_SCREEN_X_M = 0.3
SIZE_SCREEN_Y_M = 0.5

# screen ratio, aka meter/pixel
RATIO_X = SIZE_SCREEN_X_M / SIZE_SCREEN_X_PX
RATIO_Y = SIZE_SCREEN_Y_M / SIZE_SCREEN_Y_PX


# Otis hand workspace extremities and center
A=(35,107)
B=(86.5,127)
C=(125,84.5)
D=(80.5,79)
center=(80,100)


#TODO - import the x, y from the screen_pressed subscriber
#goal_x_px = #___ ?
#goal_y_px = #___ ?

#TODO - improve by calibrating depending on where the screen is
screen_x_origin = 0.15
screen_y_origin = SIZE_SCREEN_Y_M / 2
fixed_z = -0.2

"""
 calculating in reachy coordinates the destination given by the screen_pressed
 @param goal_x, goal_y : the x and y coordinates of the pixels pressed
 @return scaled_goal : the coordinates for the point usable by reachy
"""
def rescale_destination(goal_x, goal_y):

    if (goal_x < 0):
        goal_x = 0
    if (goal_x > SIZE_SCREEN_X_PX):
        goal_x = SIZE_SCREEN_X_PX
    if (goal_y < 0):
        goal_y = 0
    if (goal_y > SIZE_SCREEN_Y_PX):
        goal_y = SIZE_SCREEN_Y_PX

    goal_x_m = goal_x * RATIO_X + screen_x_origin 
    goal_y_m = screen_y_origin - goal_y * RATIO_Y 
    print("goal_x", goal_x_m, "goal_y", goal_y_m)

    scaled_goal= np.array([
        [0, 0, -1, goal_x_m],
        [0, 1, 0, goal_y_m],  
        [1, 0, 0, fixed_z],
        [0, 0, 0, 1],  
    ])

    return scaled_goal

