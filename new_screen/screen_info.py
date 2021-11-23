import numpy as np

class Screen : 

     def __init__(self) -> None :
        # default parameters
        # screen size in pixels
        self.SIZE_SCREEN_X_PX = 1080
        self.SIZE_SCREEN_Y_PX = 1920
        # screen size in meters
        self.SIZE_SCREEN_X_M = 0.3
        self.SIZE_SCREEN_Y_M = 0.5
        # screen ratio
        self.RATIO_X = self.SIZE_SCREEN_X_M / self.SIZE_SCREEN_X_PX
        self.RATIO_Y = self.SIZE_SCREEN_Y_M / self.SIZE_SCREEN_Y_PX
        # screen flat z position 
        self.fixed_z = 0
        # transformation matrices reachy to screen (r to s)
        self.translation_matrix_r_to_s = [0., 0.]
        self.rotation_matrix_r_to_s  = [[1., 0.], [0., 1.]]
        # if the screen has been calibrated yet
        self.calibrated = False

        # hand rest position
        self.rest_pos = np.array([
            [-0.17103305,  0.31634818, -0.93309781,  0.33488534],
            [-0.98353147, -0.1109781,   0.14265242, -0.29761366],
            [-0.05842559,  0.94212934,  0.33011931, -0.40],
            [ 0,          0,         0,          1,        ]
        ])





 