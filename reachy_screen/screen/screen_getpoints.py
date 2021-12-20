from screen import screen_calibration

# testing : DONE
# works : YES - DO NOT TOUCH

"""
getting the screen x and y + reachy's x and y for a point P
@param reachy : reachy
@param screen_feedback : informations from the screen regarding the last pressed points
@return arm_coords : position of the calibrated point in reachy's coordinates
"""

def get_calibration_points(screen, screen_feedback):
    # determine how many points were calibrated already
    if (screen.calib_step == 0):
        screen.A = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        screen.calib_step += 1
        print("A : ", screen.A)
    elif (screen.calib_step == 1):
        screen.B = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        if((abs(screen.B[1][0][0] - screen.A[1][0][0]) > 100) or (abs(screen.B[1][0][1] - screen.A[1][0][1]) > 100)):
            screen.calib_step += 1
            print("B : ", screen.B)
        else : 
            print("- - - recalibrate B, point too close to A - - -")    
    elif (screen.calib_step == 2):
        screen.C = [screen.reachy.r_arm.forward_kinematics(), screen_feedback[-1:]]
        if((abs(screen.C[1][0][0] - screen.A[1][0][0]) > 100) or (abs(screen.C[1][0][1] - screen.A[1][0][1]) > 100)):
            if((abs(screen.C[1][0][0] - screen.B[1][0][0]) > 100) or (abs(screen.C[1][0][1] - screen.B[1][0][1]) > 100)):       
                screen.calib_step += 1
                print("C : ", screen.C)
                screen_calibration.screen_calibration(screen)
            else :
                print("- - - recalibrate C, point too close to B - - -")
        else :
            print("- - - recalibrate C, point too close to A - - -")    
    else:
        print("- - Three points already calibrated - -")