import numpy as np

#TODO create a class for this
class Screen_Processing : 

    # screen size in pixels
    SIZE_SCREEN_X_PX = 1080  
    SIZE_SCREEN_Y_PX = 1920

    # Otis hand workspace extremities and center
    OTIS_A = (35,107)
    OTIS_B = (86.5,127)
    OTIS_C = (125,84.5)
    OTIS_D = (80.5,79)
    OTIS_CENTER = (80,100)

    """
    initiating the screen processor with the adequate values of screen size and height from the calibration
    """
    def __init__(self, screen, fixed_z) -> None :
        # screen size in meters
        self.SIZE_SCREEN_X_M = screen[0]
        self.SIZE_SCREEN_Y_M = screen[1]

         # screen ratio, aka meter/pixel
        self.RATIO_X = self.SIZE_SCREEN_X_M / self.SIZE_SCREEN_X_PX
        self.RATIO_Y = self.SIZE_SCREEN_Y_M / self.SIZE_SCREEN_Y_PX

        #TODO - improve by calibrating depending on where the screen is
        self.screen_x_origin = 0.1
        self.screen_y_origin = self.SIZE_SCREEN_Y_M / 2
        self.fixed_z = fixed_z



    #TODO - import the x, y from the screen_pressed subscriber
    #goal_x_px = #___ ?
    #goal_y_px = #___ ?

    

    """
    calculating in meters the pixel coordinates of the destination given by the screen press
    @param goal : array with the the x and y coordinates of the pixels pressed
    @return scaled_goal : array with the coordinates for the destination in meters in reachy coordinate system
    """
    def rescale_destination_pixels_to_meters(self, goal):

        # checking if the point is within the boundaries of the screen
        if (goal[0] < 0):
            goal[0] = 0
        if (goal[0] > self.SIZE_SCREEN_X_PX):
            goal[0] = self.SIZE_SCREEN_X_PX
        if (goal[1] < 0):
            goal[1] = 0
        if (goal[1] > self.SIZE_SCREEN_Y_PX):
            goal[1] = self.SIZE_SCREEN_Y_PX


        goal_x_m = goal[0] * self.RATIO_X + self.screen_x_origin 
        goal_y_m = self.screen_y_origin - goal[1] * self.RATIO_Y 
        print("goal_x", goal_x_m, "goal_y", goal_y_m)

        scaled_goal= np.array([goal_x_m, goal_y_m])  

        return scaled_goal



    """
    calculating the adequate meter coordinates based on the screen calibration
    @param goal : array with the the x and y coordinates in meters in the reachy coordinate system
    @param translation_1 : translation matrix from reachy's origin to the screen's origin 
    @param rotation : rotation matrix
    @param translation_2 : translation matrix from the "ideal" screen origin to reachy's origin
    @return calibrated_goal : array with the calibrated coordinates for the destination in meters in reachy coordinate system
    """
    def rescale_destination_to_calibration(self, goal, translation_1, rotation, translation_2): 
        #TODO : check that goal, translations are vectors and rotatio is a 2x2 matrix
        calibrated_goal = goal + translation_2
        calibrated_goal = [np.dot(calibrated_goal, rotation[0]), np.dot(calibrated_goal, rotation[1])]
        calibrated_goal = calibrated_goal + translation_1
        print("calibrated goal : ", calibrated_goal)
        return calibrated_goal



    """
    calculating the adequate matrix to use the inverse kinematics funtion of reachy based on the goal destination
    @param goal : array with the the x and y coordinates in meters pressed
    @return matrix_goal : 4d matrix with goal coordinates and motors rotation
    """
    def vector_to_matrix_press(self, goal):

        matrix_goal = np.array([
            [0, 0, -1, goal[0]],
            [0, 1, 0, goal[1]],
            [1, 0, 0, self.fixed_z], 
            [0, 0, 0, 1]
        ])

        return matrix_goal
