import numpy as np

"""
calculating in reachy's coordinates the pixel coordinates of the destination given
@param screen : information on our screen
@param goal : array with the coordinates for the destination in screen coordinates
"""
def processing_screen_point(screen, goal):

    # checking if the point is within the boundaries of the screen
    if (goal[0] < 0):
        goal[0] = 0
    if (goal[0] > screen.SIZE_SCREEN_X_PX):
        goal[0] = screen.SIZE_SCREEN_X_PX
    if (goal[1] < 0):
        goal[1] = 0
    if (goal[1] > screen.SIZE_SCREEN_Y_PX):
        goal[1] = screen.SIZE_SCREEN_Y_PX

    goal_x_m = goal[0] * screen.RATIO_X
    goal_y_m = goal[1] * screen.RATIO_Y

    scaled_goal = rescale_destination_to_calibration(screen, [goal_x_m, goal_y_m])

    return scaled_goal

    
"""
calculating the adequate meter coordinates based on the screen calibration
@param screen : information on our screen
@param goal : array with the the x and y coordinates in meters in the reachy coordinate system
@return calibrated_goal : array with the calibrated coordinates for the destination in meters in reachy coordinate system
"""
def rescale_destination_to_calibration(screen, goal): 

    calibrated_goal = [np.dot(goal[0], screen.rotation_matrix_r_to_s[0]), np.dot(goal[1], screen.rotation_matrix_r_to_s[1])]
    calibrated_goal = [calibrated_goal[0] + screen.translation_matrix_r_to_s[0], calibrated_goal[1] + screen.translation_matrix_r_to_s[1]] 
    
    return calibrated_goal
