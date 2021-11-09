import numpy as np
import keyboard
from numpy.core.numeric import True_

Z_LIMIT = 0.05
class Screen_Calibrator : 

  """
  initiating the screen calibrator with some standard values, no rotation, no translation
  """
  def __init__(self) -> None :
    self.screen = [0.5, 0.3]
    self.fixed_z = -0.2
    self.trans_mat_1 = [0., 0.]
    self.inverted_rot_mat  = [[1., 0.], [0., 1.]]
    self.trans_mat_2 = [0., 0.]
    self.flat = True


  #TODO : consider non othogonal coordinate systems and adjust accordigly (goes along with screen x y input)
  """
  initiating the calibration to use the screen in all conditions (z axis not covered, screen must lay flat)
  @param reachy : reachy, to use forward kinematics for the calibration
  """
  def calibrate_screen(self, reachy):
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
    A = calibrate_reachy_coords(reachy)
    B = calibrate_reachy_coords(reachy)
    C = calibrate_reachy_coords(reachy)

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

      # translation of the screen origin to the same origin as reachy
      translation_matrix_1 = coord_a
      t_A = [coord_a[0] - translation_matrix_1[0], coord_a[1] - translation_matrix_1[1]]
      t_B = [coord_b[0] - translation_matrix_1[0], coord_b[1] - translation_matrix_1[1]]
      t_C = [coord_c[0] - translation_matrix_1[0], coord_c[1] - translation_matrix_1[1]]

      #rotation of the screen origin to the same origin as reachy (only "feasable positions" are considered)
      if t_B[1] == 0:
        theta = np.pi / 2
      else :
        theta = np.arctan(t_B[0] / t_B[1])
      print("theta : ", theta)
      rotation_matrix = [
          [np.cos(theta), np.sin(theta)], 
          [-np.sin(theta), np.cos(theta)]
        ]
      
      # calculating new corners positions
      r_B = np.matmul(rotation_matrix, t_B)
      r_C = np.matmul(rotation_matrix, t_C)

      # screen size in accordance to the calibration
      screen_width = r_B[1]
      screen_height = r_C[0]
      screen = [abs(screen_height), abs(screen_width)]

      translation_matrix_2 = [0, abs(screen_width/2)]

      # turning rotation array into a matrix, inverting it, and back to array again
      inverted = np.linalg.inv(np.asmatrix(rotation_matrix))
      inverted_rot_mat = [[inverted[0, 0], inverted[0, 1]], [inverted[1, 0], inverted[1, 1]]]

      # updating all the values of my calibrator
      self.screen = screen
      self.fixed_z = fixed_z  
      self.trans_mat_1 = [translation_matrix_1[0], translation_matrix_1[1]]
      self.inverted_rot_mat = inverted_rot_mat
      self.trans_mat_2 = [-translation_matrix_2[0], -translation_matrix_2[1]]


#TODO : get the x and y of the screen at the same time to make calibration more modular
def calibrate_reachy_coords(reachy) : 
  text = input("Press ENTER to calibrate point : ")
  while True :
        if text == "":
            arm_coords = reachy.r_arm.forward_kinematics()
            break
        else :
            text = input("Pres ONLY the ENTER key to calibrate the point : ") 

  return arm_coords