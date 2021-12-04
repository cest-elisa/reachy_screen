from reachy_sdk import ReachySDK
import numpy as np

class Screen : 

     def __init__(self) -> None :
         
         self.reachy =  ReachySDK(host='127.0.0.1') 

         # default parameters
         # screen size in pixels
         self.SIZE_SCREEN_X_PX = 1920
         self.SIZE_SCREEN_Y_PX = 1080
         self.PIXEL_SIZE = 0

         # screen size in meters
         self.SIZE_SCREEN_X_M = 0.3
         self.SIZE_SCREEN_Y_M = 0.5
         
         self.RATIO_X = self.SIZE_SCREEN_X_M / self.SIZE_SCREEN_X_PX
         self.RATIO_Y = self.SIZE_SCREEN_Y_M / self.SIZE_SCREEN_Y_PX
         
         # avoid useless calulations
         self.sizes_updated = False

         # screen flat z position 
         self.fixed_z = 0

         # transformation matrices reachy to screen (r to s)
         self.translation_matrix_r_to_s = [0., 0.]
         self.rotation_matrix_r_to_s  = [[1., 0.], [0., 1.]]

         # if the screen has been calibrated yet
         self.calibrated = False

         # three base calibration points
         self.A = []
         self.B = []
         self.C = []
         self.calib_step = 0

         # hand rest position
         self.rest_pos = np.array([[-0.15616132,  0.2448566,  -0.95690067,  0.27631352],
                                    [-0.98245875,  0.06146337,  0.17605983, -0.39589202],
                                    [ 0.10192375,  0.96760917,  0.23096331, -0.42      ],
                                    [ 0.,          0.,          0.,          1.        ]]
         )