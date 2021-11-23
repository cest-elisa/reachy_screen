import numpy as np
import math

Z_LIMIT = 0.05

# actually does not work, have to give it the feedback "live" aaaaaaaaaaaaaaaaa
# how do i do thiiis, frick frack

"""
  initiating the calibration to use the screen in all conditions (z axis not covered, screen must lay flat)
  @param reachy : reachy, to use forward kinematics for the calibration
"""
def screen_calibration(reachy, screen, screen_feedback): 

    calib_A = calibrate_on_enter(reachy, screen_feedback)
    print("A = ", calib_A)
    calib_B = calibrate_on_enter(reachy, screen_feedback)
    print("B = ", calib_B)
    calib_C = calibrate_on_enter(reachy, screen_feedback)
    print("C = ", calib_C)


    A = calib_A[0]
    B = calib_B[0]
    C = calib_C[1]

    # extracting the x and y reachy coordinates of the screen corners
    coord_a = [A[0, 3], A[1, 3]]
    coord_b = [B[0, 3], B[1, 3]]
    coord_c = [C[0, 3], C[1, 3]]
    print("A = ", coord_a, A[2, 3])
    print("B = ", coord_b, B[2, 3])
    print("C = ", coord_c, C[2, 3])


    # fixed z position for touching the screen ; if the z difference is too big, asks to place the screen on flat surface
    if (abs(A[2, 3] - B[2, 3]) > Z_LIMIT) or (abs(C[2, 3] - B[2, 3]) > Z_LIMIT) or (abs(A[2, 3] - C[2, 3]) > Z_LIMIT) :
        print("Please place the screen on a flat surface and try again")
    else : 
        # taking the average of all 3 calibrations, plus some extra height for safety
        fixed_z = np.mean([A[2, 3], B[2, 3], C[2, 3]]) + 0.03

        # triangulation of the screen corners
        D = triangulate_point(screen, [0, 0], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )
        E = triangulate_point(screen, [0, screen.SIZE_SCREEN_Y_PX], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )
        F = triangulate_point(screen, [screen.SIZE_SCREEN_X_PX, 0], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )

        # translation of the screen origin to reachy's coordinates
        translation_matrix_1 = D
        t_A = [D[0] - translation_matrix_1[0], D[1] - translation_matrix_1[1]]
        t_B = [E[0] - translation_matrix_1[0], E[1] - translation_matrix_1[1]]
        t_C = [F[0] - translation_matrix_1[0], F[1] - translation_matrix_1[1]]

        # rotation of the screen origin to the same origin as reachy (only "feasable positions" are considered)
        if t_B[1] == 0:
            theta = np.pi / 2
        else :
            theta = np.arctan(t_B[0] / t_B[1])
        print("theta : ", theta)
        rotation_matrix = [
            [np.cos(theta), np.sin(theta)], 
            [-np.sin(theta), np.cos(theta)]
        ]

        # turning rotation array into a matrix, inverting it, and back to array again
        inverted = np.linalg.inv(np.asmatrix(rotation_matrix))
        inverted_rot_mat = [[inverted[0, 0], inverted[0, 1]], [inverted[1, 0], inverted[1, 1]]]

        # updating screen information
        screen.fixed_z = fixed_z  
        screen.translation_matrix_r_to_s = [translation_matrix_1[0], translation_matrix_1[1]]
        screen.rotation_matrix_r_to_s = inverted_rot_mat
        screen.calibrated = True
    return







"""
  triangulating the corners of the screen from any three points A, B and C [Snellius-Pothenot problem]
  only known parameter : screen size in pixels
  for calculations see "calculation/coord_triangulation.png"
  @param screen_dest : corner point we want to triangulate
  @param screen_A, screen_B, screen_C : x, y pixel coordinates of A, B and C according to the screen's origin
  @param reachy_A, reachy_B, reachy_C : x, y meter coordinates of A, B and C according to reachy's origin
  @return reachy_dest : x, y meter coordinates of the corner 
 """
def triangulate_point(screen, screen_dest, screen_A, screen_B, screen_C, reachy_A, reachy_B, reachy_C):
    # calculating the size of a pixel
    screen_AB = math.sqrt(pow(screen_A[0] - screen_B[0], 2) + pow(screen_A[1] - screen_B[1], 2))
    reachy_AB = math.sqrt(pow(reachy_A[0] - reachy_B[0], 2) + pow(reachy_A[1] - reachy_B[1], 2))
    px_size = reachy_AB / screen_AB

    # updating screen informations
    screen.SIZE_SCREEN_X_M = screen.SIZE_SCREEN_X_PX * px_size
    screen.SIZE_SCREEN_Y_M = screen.SIZE_SCREEN_Y_PX * px_size
    screen.RATIO_X = screen.SIZE_SCREEN_X_M / screen.SIZE_SCREEN_X_PX
    screen.RATIO_Y = screen.SIZE_SCREEN_Y_M / screen.SIZE_SCREEN_Y_PX


    # calculating distance in meters between points and destination
    screen_AO = math.sqrt(pow(screen_A[0] - screen_dest[0], 2) + pow(screen_A[1] - screen_dest[1], 2))
    reachy_AO = screen_AO * px_size
    screen_BO = math.sqrt(pow(screen_B[0] - screen_dest[0], 2) + pow(screen_B[1] - screen_dest[1], 2))
    reachy_BO = screen_BO * px_size
    screen_CO = math.sqrt(pow(screen_C[0] - screen_dest[0], 2) + pow(screen_C[1] - screen_dest[1], 2))
    reachy_CO = screen_CO * px_size

    # matrix calculation for Mx = b
    M = [[2*(reachy_B[0] - reachy_A[0]), 2*(reachy_B[1] - reachy_A[1])], 
        [2*(reachy_C[0] - reachy_A[0]), 2*(reachy_C[1] - reachy_A[1])]]
    b = [pow(reachy_A[0], 2) - pow(reachy_B[0], 2) + pow(reachy_A[1], 2) - pow(reachy_B[1], 2) - pow(reachy_AO, 2) + pow(reachy_BO, 2),
        pow(reachy_A[0], 2) - pow(reachy_C[0], 2) + pow(reachy_A[1], 2) - pow(reachy_C[1], 2) - pow(reachy_AO, 2) + pow(reachy_CO, 2)]

    # matrix calculation for x = M^-1 * b
    reachy_dest = np.matmul(np.linalg.inv(M), b)

    return reachy_dest






"""
getting the screen x and y + reachy's x and y for a point P
@param reachy : reachy
@param screen_feedback : informations from the screen regarding the last pressed points
@return arm_coords : position of the calibrated point in reachy's coordinates
"""
def calibrate_on_enter(reachy, screen_feedback):
    text = input("Press ENTER to calibrate point : ")
    while True :
        if text == "":
            arm_coords = reachy.r_arm.forward_kinematics()
            screen_coord = screen_feedback[-2:]
            break
        else :
            text = input("Pres ONLY the ENTER key to calibrate the point : ") 

    return [arm_coords, screen_coord]
