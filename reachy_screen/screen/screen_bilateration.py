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

def bilaterate_point(screen, screen_dest, screen_A, screen_B, screen_C, reachy_A, reachy_B, reachy_C):
    print("- - - - - - point - - - - - -")
    print("in bilateration for point : ", screen_dest)

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
    screen_AO = math.sqrt(math.pow(screen_A[0] - screen_dest[0], 2) + math.pow(screen_A[1] - screen_dest[1], 2))
    reachy_AO = screen_AO * screen.PIXEL_SIZE
    screen_BO = math.sqrt(math.pow(screen_B[0] - screen_dest[0], 2) + math.pow(screen_B[1] - screen_dest[1], 2))
    reachy_BO = screen_BO * screen.PIXEL_SIZE
    screen_CO = math.sqrt(math.pow(screen_C[0] - screen_dest[0], 2) + math.pow(screen_C[1] - screen_dest[1], 2))
    reachy_CO = screen_CO * screen.PIXEL_SIZE

    sols_AB = two_circle_intersection(reachy_AO, reachy_A[0], reachy_A[1], reachy_BO, reachy_B[0], reachy_B[1])
    sols_AC = two_circle_intersection(reachy_AO, reachy_A[0], reachy_A[1], reachy_CO, reachy_C[0], reachy_C[1])

    print("solustions for AB intersection : ", sols_AB)
    print("solustions for AC intersection : ", sols_AC)

    # taking the solution closest together
    reachy_destination = [(sols_AB[0][0] + sols_AC[0][0])/2, (sols_AB[0][1] + sols_AC[0][1])/2]
    min_dist = abs(sols_AB[0][0] - sols_AC[0][0]) + abs(sols_AB[0][1] - sols_AC[0][1])

    if(abs(sols_AB[0][0] - sols_AC[1][0]) + abs(sols_AB[0][1] - sols_AC[1][1] < min_dist)):
        reachy_destination = [(sols_AB[0][0] + sols_AC[1][0])/2, (sols_AB[0][1] + sols_AC[1][1])/2]
    elif(abs(sols_AB[1][0] - sols_AC[0][0]) + abs(sols_AB[1][1] - sols_AC[0][1]) < min_dist):
        reachy_destination = [(sols_AB[1][0] + sols_AC[0][0])/2, (sols_AB[1][1] + sols_AC[0][1])/2]
    elif(abs(sols_AB[1][0] - sols_AC[1][0]) + abs(sols_AB[1][1] - sols_AC[1][1])):
        reachy_destination = [(sols_AB[1][0] + sols_AC[1][0])/2, (sols_AB[1][1] + sols_AC[1][1])/2]

    print("reachy destination : ", reachy_destination)
    return reachy_destination



"""
  intersection points of two circles
  calculations taken from : https://members.loria.fr/DRoegel/loc/note0001.pdf
  @param r1, r2 : radiuses of the two circles
  @param x1, y1, x2, y2 : coordinates of the centers of the two circles
  @return sol_1, sol_2 : array with the two possible intersection points
 """
def two_circle_intersection(r1, x1, y1, r2, x2, y2):
    print(r1, x1, y1, r2, x2, y2)
    a = 2 * (x2 - x1)
    b = 2 * (y2 - y1)
    c = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) - math.pow(r2, 2) + math.pow(r1, 2)
    delta = abs(math.pow(2*(a)*(c), 2) - 4 * (math.pow(a, 2) + math.pow(b, 2))*(math.pow(c, 2) - math.pow(b, 2) * math.pow(r1, 2)))
    print("a : ", a, "   b : ", b, "   c : ", c, "  delta : ", delta)

    sol1_x = x1 + ((2*a*c - math.sqrt(delta))/(2*(a*a + b*b)))
    sol1_y = y1 + ((c - a*(sol1_x-x1))/b)
    sol2_x = x1 + ((2*a*c + math.sqrt(delta))/(2*(a*a + b*b)))
    sol2_y = y1 + ((c - a*(sol2_x-x1))/b)

    return [[sol1_x, sol1_y], [sol2_x, sol2_y]]