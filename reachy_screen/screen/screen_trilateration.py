import numpy as np
import math

"""
  trilaterating the corners of the screen from any three points A, B and C [Snellius-Pothenot problem ?]
  only known parameter : screen pixel resolution
  for calculations see "calculation/coord_triangulation.png"
  @param screen_dest : corner point we want to triangulate
  @param screen_A, screen_B, screen_C : x, y pixel coordinates of A, B and C according to the screen's origin
  @param reachy_A, reachy_B, reachy_C : x, y meter coordinates of A, B and C according to reachy's origin
  @return reachy_dest : x, y meter coordinates of the desired screen_dest 
 """

def trilaterate_point(screen, screen_dest, screen_A, screen_B, screen_C, reachy_A, reachy_B, reachy_C):
    print("- - - - - - point - - - - - -")
    print("in trilateration for point : ", screen_dest)

    # calculating the screen informations and updating them once
    if(screen.sizes_updated == False):

        # calculating the size of a pixel
        screen_AB = math.sqrt(pow(screen_B[0] - screen_A[0], 2) + pow(screen_B[1] - screen_A[1], 2))
        reachy_AB = math.sqrt(pow(reachy_B[0] - reachy_A[0], 2) + pow(reachy_B[1] - reachy_A[1], 2))
        screen.PIXEL_SIZE = reachy_AB / screen_AB
        print("screen AB = ",  screen_AB)
        print("reachy AB = ", reachy_AB)

        # updating screen information
        print("screen size before : ", screen.SIZE_SCREEN_X_M, screen.SIZE_SCREEN_Y_M)
        screen.SIZE_SCREEN_X_M = screen.SIZE_SCREEN_X_PX * screen.PIXEL_SIZE
        screen.SIZE_SCREEN_Y_M = screen.SIZE_SCREEN_Y_PX * screen.PIXEL_SIZE
        screen.sizes_updated = True
        print("screen size after : ", screen.SIZE_SCREEN_X_M, screen.SIZE_SCREEN_Y_M)

    # calculating distance in meters between points and destination
    screen_AO = math.sqrt(pow(screen_A[0] - screen_dest[0], 2) + pow(screen_A[1] - screen_dest[1], 2))
    reachy_AO = screen_AO * screen.PIXEL_SIZE
    screen_BO = math.sqrt(pow(screen_B[0] - screen_dest[0], 2) + pow(screen_B[1] - screen_dest[1], 2))
    reachy_BO = screen_BO * screen.PIXEL_SIZE
    screen_CO = math.sqrt(pow(screen_C[0] - screen_dest[0], 2) + pow(screen_C[1] - screen_dest[1], 2))
    reachy_CO = screen_CO * screen.PIXEL_SIZE
    print("screen AO = ",  screen_AO)
    print("reachy AO = ", reachy_AO)
    print("screen BO = ",  screen_BO)
    print("reachy BO = ", reachy_BO)
    print("screen CO = ",  screen_CO)
    print("reachy CO = ", reachy_CO)

    # matrix calculation for Mx = b
    M = [[2*(reachy_B[0] - reachy_A[0]), 2*(reachy_B[1] - reachy_A[1])], 
        [2*(reachy_C[0] - reachy_A[0]), 2*(reachy_C[1] - reachy_A[1])]]
    b = [pow(reachy_AO, 2) - pow(reachy_BO, 2) - pow(reachy_A[0], 2) + pow(reachy_B[0], 2) - pow(reachy_A[1], 2) + pow(reachy_B[1], 2), 
         pow(reachy_AO, 2) - pow(reachy_CO, 2) - pow(reachy_A[0], 2) + pow(reachy_C[0], 2) - pow(reachy_A[1], 2) + pow(reachy_C[1], 2)]
    #b = [pow(reachy_A[0], 2) - pow(reachy_B[0], 2) + pow(reachy_A[1], 2) - pow(reachy_B[1], 2) - pow(reachy_AO, 2) + pow(reachy_BO, 2),
    #    pow(reachy_A[0], 2) - pow(reachy_C[0], 2) + pow(reachy_A[1], 2) - pow(reachy_C[1], 2) - pow(reachy_AO, 2) + pow(reachy_CO, 2)]
    
    # least square solution to M * x = b
    reachy_dest = np.linalg.lstsq(M, b, rcond=None)
    #reachy_dest = np.matmul(np.linalg.inv(M), b)
    print("reachy destination coords = ", reachy_dest[0])
    
    return reachy_dest[0]