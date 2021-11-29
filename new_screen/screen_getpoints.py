"""
getting the screen x and y + reachy's x and y for a point P
@param reachy : reachy
@param screen_feedback : informations from the screen regarding the last pressed points
@return arm_coords : position of the calibrated point in reachy's coordinates
"""

# I Think it still does not work to get real time information :(( 
def calibrate_on_enter(reachy, screen, screen_feedback):
    text = input("Press ENTER to calibrate point : ")
    while True :
        if text == "":
            # determine how many points were calibrated already
            if (screen.calib_step == 0):
                screen.A = [reachy.r_arm.forward_kinematics(), screen_feedback[-2:]]
                screen.calib_step += 1
                break
            elif (screen.calib_step == 1):
                screen.B = [reachy.r_arm.forward_kinematics(), screen_feedback[-2:]]
                screen.calib_step += 1
                break
            elif (screen.calib_step == 2):
                screen.C = [reachy.r_arm.forward_kinematics(), screen_feedback[-2:]]
                screen.calib_step += 1
                break
            else:
                print("three points already calibrated")
        else :
            text = input("Pres ONLY the ENTER key to calibrate the point : ") 