import numpy as np

# testing : DONE
# works : YES, DO NOT TOUCH

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

    # scaling goal point to meters based on the screen's pixel size
    goal_x_m = goal[0] * screen.PIXEL_SIZE
    goal_y_m = goal[1] * screen.PIXEL_SIZE

    scaled_goal = rescale_destination_to_calibration(screen, [goal_x_m, goal_y_m])

    return scaled_goal

    


"""
  calculating the adequate meter coordinates based on the screen calibration
  @param screen : information on our screen
  @param goal : array with the the x and y coordinates in meters in the reachy coordinate system
  @return calibrated_goal : array with the calibrated coordinates for the destination in meters in reachy coordinate system
"""

def rescale_destination_to_calibration(screen, goal):

    print("goal : ", goal)
    calibrated_goal = [np.dot(screen.rotation_matrix_r_to_s[0], goal), np.dot(screen.rotation_matrix_r_to_s[1], goal)]  
    print("rotated goal : ", calibrated_goal)
    calibrated_goal = [calibrated_goal[0] + screen.translation_matrix_r_to_s[0], calibrated_goal[1] + screen.translation_matrix_r_to_s[1]] 
    print("translated goal : ", calibrated_goal)

    return calibrated_goal