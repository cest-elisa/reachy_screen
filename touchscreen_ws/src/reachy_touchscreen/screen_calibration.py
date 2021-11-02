import numpy as np

#TODO : change and use reachy hand for calibration
s_a, s_b, s_c, t_a, t_b, t_c, z_a, z_b, z_c = 0.2

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

def calibrate_screen():
    #TODO : implement forward kinematics to get motors --> to coord 
    #TODO : figure out how to get the 3 motor thingies
    coord_a = np.array[A[0, 3], A[1 ,3]]
    coord_b = np.array[B[0, 3], B[1 ,3]]
    coord_c = np.array[C[0, 3], C[1 ,3]]


    #fixed z position for touching the screen (assumes the screen is laying flat)
    fixed_z = np.mean(np.array[A[2, 3], B[2, 3], C[2, 3]])

    # translation of the screen origin to the same origin as reachy
    translation_matrix_1 = coord_a
    t_A = coord_a - translation_matrix_1
    t_B = coord_b - translation_matrix_1
    t_C = coord_c - translation_matrix_1

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
    screen = np.array[screen_width, screen_height]

    translation_matrix_2 = np.array[0, screen_width/2]

    return [fixed_z, translation_matrix_1, rotation_matrix, translation_matrix_2, screen]


