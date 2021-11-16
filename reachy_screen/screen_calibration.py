from numpy.core.numeric import True_
import numpy as np
import math
from numpy.core.numerictypes import sctype2char

Z_LIMIT = 0.05
SIZE_SCREEN_X_PX = 1080  
SIZE_SCREEN_Y_PX = 1920

class Screen_Calibrator : 

  """
  initiating the screen calibrator with some standard values, no rotation, no translation
  """
  def __init__(self) -> None :
    self.screen = [0.5, 0.3]
    self.fixed_z = -0.2
    self.trans_mat_1 = [0., 0.]
    self.inverted_rot_mat  = [[1., 0.], [0., 1.]]
    self.flat = True
    self.done = False


  """
  initiating the calibration to use the screen in all conditions (z axis not covered, screen must lay flat)
  @param reachy : reachy, to use forward kinematics for the calibration
  """
  def calibrate_screen(self, reachy, screen_positions):
    '''
    # used for testing without reachy{
      s_a = 0
      s_b = 0.8
      s_c = 0
      t_a = 0
      t_b = 0
      t_c = 0.5
      z_a = 0.0 
      z_b = 0.0 
      z_c = 0.0

      A = np.array([
        [1, 0, 0, s_a],
        [0, 1, 0, t_a],  
        [0, 0, 1, z_a],
        [0, 0, 0, 1],  
      ])
      B = np.array([
        [1, 0, 0, s_b],
        [0, 1, 0, t_b],  
        [0, 0, 1, z_b],
        [0, 0, 0, 1],  
      ])
      C = np.array([
        [1, 0, 0, s_c],
        [0, 1, 0, t_c],  
        [0, 0, 1, z_c],
        [0, 0, 0, 1],  
      ])
    }
    '''

    #TODO : test
    calib_A = calibrate_reachy_coords(reachy, screen_positions)
    print("A = ", calib_A)
    calib_B = calibrate_reachy_coords(reachy, screen_positions)
    print("B = ", calib_B)
    calib_C = calibrate_reachy_coords(reachy, screen_positions)
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
      self.flat = False
    else : 
      # taking the average of all 3 calibrations, plus some extra height for safety
      fixed_z = np.mean([A[2, 3], B[2, 3], C[2, 3]]) + 0.03

      # triangulation of the screen corners
      D = corner_triangulation(self, [0, 0], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )
      E = corner_triangulation(self, [0, SIZE_SCREEN_Y_PX], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )
      F = corner_triangulation(self, [SIZE_SCREEN_X_PX, 0], calib_A[1], calib_B[1], calib_C[1], coord_a, coord_b, coord_c )

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

      # updating all the values of my calibrator
      self.fixed_z = fixed_z  
      self.trans_mat_1 = [translation_matrix_1[0], translation_matrix_1[1]]
      self.inverted_rot_mat = inverted_rot_mat
      self.done = True




"""
  triangulating the corners of the screen from any three points A, B and C
  only known parameter : screen size in pixels
  for calculations see "coord_triangulation.png"
  @param screen_dest : corner point we want to triangulate
  @param screen_A, screen_B, screen_C : x, y pixel coordinates of A, B and C according to the screen's origin
  @param reachy_A, reachy_B, reachy_C : x, y meter coordinates of A, B and C according to reachy's origin
  @return reachy_dest : x, y meter coordinates of the corner 
 """
def corner_triangulation(calibrator, screen_dest, screen_A, screen_B, screen_C, reachy_A, reachy_B, reachy_C):
  # calculating the size of a pixel
  screen_AB = math.sqrt(pow(screen_A[0] - screen_B[0], 2) + pow(screen_A[1] - screen_B[1], 2))
  reachy_AB = math.sqrt(pow(reachy_A[0] - reachy_B[0], 2) + pow(reachy_A[1] - reachy_B[1], 2))
  px_size = reachy_AB / screen_AB

  calibrator.screen = [SIZE_SCREEN_X_PX * px_size, SIZE_SCREEN_Y_PX * px_size]

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
getting the x and y from reachy's arm with forward kinematics
@param reachy : reachy
"""
#TODO : get the x and y of the screen at the same time to make calibration more modular
def calibrate_reachy_coords(reachy, screen_pos) : 
  text = input("Press ENTER to calibrate point : ")
  while True :
        if text == "":
            arm_coords = reachy.r_arm.forward_kinematics()
            screen_coord = screen_pos[-2:]
            break
        else :
            text = input("Pres ONLY the ENTER key to calibrate the point : ") 

  return [arm_coords, screen_coord]




