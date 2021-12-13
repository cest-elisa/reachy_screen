from screen import screen_trilateration
from screen import screen_bilateration
from screen import screen_new_trilateration
import numpy as np

# limit for the average z calibration error
Z_LIMIT = 0.05

"""
  initiating the calibration to use the screen in all conditions (z axis not covered, screen must lay flat)
  @param screen : all the screen information
"""
def screen_calibration(screen): 

    if(screen.calib_step == 3):
        A = screen.A[0]
        B = screen.B[0]
        C = screen.C[0]

        # extracting the x and y reachy coordinates of the screen corners
        coord_a = [A[0, 3], A[1, 3]]
        coord_b = [B[0, 3], B[1, 3]]
        coord_c = [C[0, 3], C[1, 3]]
       
        # fixed z position for touching the screen ; if the z difference is too big, asks to place the screen on flat surface
        if (abs(A[2, 3] - B[2, 3]) > Z_LIMIT) or (abs(C[2, 3] - B[2, 3]) > Z_LIMIT) or (abs(A[2, 3] - C[2, 3]) > Z_LIMIT) :
            print("Please place the screen on a flat surface and try again")
            print("- - - - - - calibration in process - - - - - -")
            screen.calib_step = 0

        else : 
            # taking the average of all 3 calibrations, plus some extra height for safety
            fixed_z = np.mean([A[2, 3], B[2, 3], C[2, 3]])

            D = screen_new_trilateration.trilaterate_point(screen, [0, 0], screen.A[1][0], screen.B[1][0], screen.C[1][0], coord_a, coord_b, coord_c)
            F = screen_new_trilateration.trilaterate_point(screen, [screen.SIZE_SCREEN_X_PX, 0], screen.A[1][0], screen.B[1][0], screen.C[1][0], coord_a, coord_b, coord_c)
            E = screen_new_trilateration.trilaterate_point(screen, [0, screen.SIZE_SCREEN_Y_PX], screen.A[1][0], screen.B[1][0], screen.C[1][0], coord_a, coord_b, coord_c)

            # translation of the screen origin to reachy's coordinates
            translation_matrix = D
            t_E = [E[0] - translation_matrix[0], E[1] - translation_matrix[1]]

            # rotation of the screen origin to the same origin as reachy (only "feasable positions" are considered)
            if t_E[0] == 0:
                theta = np.pi / 2
            else :
                theta = np.arctan(t_E[0] / t_E[1])
            print("theta : ", theta)
            rotation_matrix = [
                [np.cos(theta), - np.sin(theta)], 
                [np.sin(theta), np.cos(theta)]
            ]

            # turning rotation array into a matrix, inverting it, and back to array again
            inverted = np.linalg.inv(np.asmatrix(rotation_matrix))
            inverted_rot_mat = [[inverted[0, 0], inverted[0, 1]], [inverted[1, 0], inverted[1, 1]]]

            print("translation matrix : ", translation_matrix)
            print("rotation matrix : ", rotation_matrix)
            print("inverse rotation matrix : ", inverted_rot_mat)


            # updating screen information
            screen.fixed_z = fixed_z  
            screen.translation_matrix_r_to_s = translation_matrix
            screen.rotation_matrix_r_to_s = inverted_rot_mat
            #screen.rotation_matrix_r_to_s = rotation_matrix
            screen.calibrated = True
    return