import numpy as np

class Screen_Calibrator : 

  """
  initiating the calibration to use the screen in all conditions (z axis not covered, screen must lay flat)
  """
  def calibrate_screen():
    #TODO : implement forward kinematics to get motors --> to coord 
    #TODO : figure out how to get the 3 motor thingies
    #TODO : change and use reachy hand for calibration
    s_a = 0
    s_b = 0
    s_c = 0.5
    t_a = 0.2
    t_b = -0.6
    t_c = 0.2
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

    coord_a = [A[0, 3], A[1, 3]]
    coord_b = [B[0, 3], B[1, 3]]
    coord_c = [C[0, 3], C[1, 3]]



    #TODO : if the distance is too big say to recalibrate the screen
    #TODO : maybe take the min instead of the average to avoid pressing too hard
    #fixed z position for touching the screen (assumes the screen is laying flat)
    fixed_z = np.mean([A[2, 3], B[2, 3], C[2, 3]])

    # translation of the screen origin to the same origin as reachy
    translation_matrix_1 = coord_a
    t_A = [coord_a[0] - translation_matrix_1[0], coord_a[1] - translation_matrix_1[1]]
    t_B = [coord_b[0] - translation_matrix_1[0], coord_b[1] - translation_matrix_1[1]]
    t_C = [coord_c[0] - translation_matrix_1[0], coord_c[1] - translation_matrix_1[1]]

    #rotation of the screen origin to the same origin as reachy
    theta = np.arctan(t_B[0] / t_B[1])
    rotation_matrix = [
        [np.cos(theta), np.sin(theta)], 
        [-np.sin(theta), np.cos(theta)]
      ]
      
    r_B = np.matmul(rotation_matrix, t_B)
    r_C = np.matmul(rotation_matrix, t_C)

    #screen size in accordance to the calibration
    screen_width = r_B[1]
    screen_height = r_C[0]
    screen = [abs(screen_width), abs(screen_height)]

    translation_matrix_2 = [0, screen_width/2]

    print("trans_mat 1 : ", translation_matrix_1)
    print("rot_mat : ", rotation_matrix)
    print("trans_mat 2 : ", translation_matrix_2)
    print("screen : ", screen)

    #turning arrays into matrices, inverting them, and back to arrays again
    inverted_rot_mat = np.asarray(np.linalg.inv(np.asmatrix(rotation_matrix)))
    inverted_rot_mat = [inverted_rot_mat[0], inverted_rot_mat[1]]
   
    print("INV rot_mat : ", inverted_rot_mat)

    return screen, fixed_z, -translation_matrix_1, inverted_rot_mat, -translation_matrix_2

