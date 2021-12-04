from screen import screen_calibration

"""
getting the screen x and y + reachy's x and y for a point P
@param reachy : reachy
@param screen_feedback : informations from the screen regarding the last pressed points
@return arm_coords : position of the calibrated point in reachy's coordinates
"""
# I Think it still does not work to get real time information :(( 
def get_calibration_points(screen, screen_feedback):
    # determine how many points were calibrated already
    if (screen.calib_step == 0):
        print("0")
        screen.A = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        print("1")
        screen.calib_step += 1
        print(screen.A)
    elif (screen.calib_step == 1):
        screen.B = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        screen.calib_step += 1
        print(screen.B)
    elif (screen.calib_step == 2):
        screen.C = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        screen.calib_step += 1
        print(screen.C)
        screen_calibration.screen_calibration(screen)
    else:
        print("three points already calibrated")