import numpy as np
import math

# testing : DONE 
# works : YES, DO NOT TOUCH

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
        screen_AC = math.sqrt(pow(screen_C[0] - screen_A[0], 2) + pow(screen_C[1] - screen_A[1], 2))
        reachy_AC = math.sqrt(pow(reachy_C[0] - reachy_A[0], 2) + pow(reachy_C[1] - reachy_A[1], 2))
        screen_CB = math.sqrt(pow(screen_B[0] - screen_C[0], 2) + pow(screen_B[1] - screen_C[1], 2))
        reachy_CB = math.sqrt(pow(reachy_B[0] - reachy_C[0], 2) + pow(reachy_B[1] - reachy_C[1], 2))

        screen.PIXEL_SIZE = (reachy_AB / screen_AB + reachy_AC / screen_AC + reachy_CB / screen_CB) / 3.

        # updating screen information
        screen.SIZE_SCREEN_X_M = screen.SIZE_SCREEN_X_PX * screen.PIXEL_SIZE
        screen.SIZE_SCREEN_Y_M = screen.SIZE_SCREEN_Y_PX * screen.PIXEL_SIZE
        screen.sizes_updated = True

    # calculating distance in meters between points and destination

    # TODO 

    # calculating distance in meters between points and destination
    screen_AO = math.sqrt(pow(screen_A[0] - screen_dest[0], 2) + pow(screen_A[1] - screen_dest[1], 2))
    reachy_AO = screen_AO * screen.PIXEL_SIZE
    screen_BO = math.sqrt(pow(screen_B[0] - screen_dest[0], 2) + pow(screen_B[1] - screen_dest[1], 2))
    reachy_BO = screen_BO * screen.PIXEL_SIZE
    screen_CO = math.sqrt(pow(screen_C[0] - screen_dest[0], 2) + pow(screen_C[1] - screen_dest[1], 2))
    reachy_CO = screen_CO * screen.PIXEL_SIZE
    # TODO

    reachy_dest = three_circle_intersection(reachy_A[0], reachy_A[1], reachy_AO, reachy_B[0], reachy_B[1], reachy_BO, reachy_C[0], reachy_C[1], reachy_CO)

    return reachy_dest







"""
  calculating the intersection point of three circles ; 
    --> we increase the EPSILON until a solution is found (the bigger the epsilon, the less accurate)
  @param x_i, y_i : origin points for the center of the circle i
  @param r_i : radius of the circle i
  @return final_intersection : final estimated intersection point for the three circles
 """

def three_circle_intersection(x0, y0, r0, x1, y1, r1, x2, y2, r2):

    EPSILON = 0.001

    # vertical and horizontal distances between the circle centers
    dx = x1 - x0
    dy = y1 - y0

    # straight-line distance between the centers
    d = math.sqrt((dy*dy) + (dx*dx))


    # 'point 2' is the point where the line through the circle intersection points crosses the line between the circle centers
    # distance from point 0 to point 2
    a = ((r0*r0) - (r1*r1) + (d*d)) / (2.0 * d)

    # coordinates of point 2 
    point2_x = x0 + (dx * a/d)
    point2_y = y0 + (dy * a/d)

    # distance from point 2 to either of the intersection points
    h = math.sqrt(abs((r0*r0) - (a*a)))

    # offsets of the intersection points from point 2
    rx = -dy * (h/d)
    ry = dx * (h/d)

    # absolute intersection points
    intersection_point1_x = point2_x + rx
    intersection_point2_x = point2_x - rx
    intersection_point1_y = point2_y + ry
    intersection_point2_y = point2_y - ry

    # determining if circle 3 intersects at either of the above intersection points
    dx = intersection_point1_x - x2
    dy = intersection_point1_y - y2
    d1 = math.sqrt((dy*dy) + (dx*dx))

    dx = intersection_point2_x - x2
    dy = intersection_point2_y - y2
    d2 = math.sqrt((dy*dy) + (dx*dx))

    final_intersection = [0, 0]
    found = False

    while(found == False):
        if(abs(d1 - r2) < EPSILON):
            print("INTERSECTION Circle1 AND Circle2 AND Circle3 : (", intersection_point1_x, ",", intersection_point1_y, ")")
            final_intersection = [intersection_point1_x, intersection_point1_y]
            found = True
        elif(abs(d2 - r2) < EPSILON):
            print("INTERSECTION Circle1 AND Circle2 AND Circle3 : (", intersection_point2_x, ",", intersection_point2_y, ")")
            final_intersection = [intersection_point2_x, intersection_point2_y]
            found = True
        else:
            EPSILON = EPSILON * 5
            
    print("accuracy epsilon : ", EPSILON)
    return final_intersection

    print("- - - - - - - - - - - - - - ")




""" testing 

def main(args=None):
    pouet = three_circle_intersection(10, 8, 4, 10, 6, (10 - 4.7889), 6, 8, (8-0.214))
    print("intersection : ", pouet)
    
if __name__ == '__main__':
  main()
"""