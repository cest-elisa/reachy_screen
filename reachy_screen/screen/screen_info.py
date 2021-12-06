"""
  class containing all the necessary information regarding the screen currently in use to interact with Reachy
  intialized with default parameters, and updated throughout the calibration process 
"""
# change screen resolution here if needed
SCREEN_RESOLUTION_X = 1920
SCREEN_RESOLUTION_Y = 1080

class Screen : 

     def __init__(self) -> None :
         
         self.reachy = None

         # screen size in pixels
         self.SIZE_SCREEN_X_PX = SCREEN_RESOLUTION_Y
         self.SIZE_SCREEN_Y_PX = SCREEN_RESOLUTION_X
         self.PIXEL_SIZE = 0

         # screen size in meters
         self.SIZE_SCREEN_X_M = 0.3
         self.SIZE_SCREEN_Y_M = 0.5
         
         # avoid useless calulations
         self.sizes_updated = False

         # screen laying flat - z position 
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
         self.rest_pos = None