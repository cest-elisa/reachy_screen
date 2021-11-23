from operator import pos
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np
from reachy_screen.screen_calibration import Screen_Calibrator
from reachy_screen.screen_processing import Screen_Processing

#TODO later : make  the head look at the head ? 
#TODO later : check the temperatures all along to avoid frying some motors
#TODO later : choose which arm moves depending on the distance from goal
#TODO later : choose if otis hand moves or the arm moves depending on distance from goal

#call at the beggining of a funtion everything that is "outside"
reachy = ReachySDK(host='127.0.0.1') 
positions = []

REST_COORD = np.array([
  [-0.17103305,  0.31634818, -0.93309781,  0.33488534],
  [-0.98353147, -0.1109781,   0.14265242, -0.29761366],
  [-0.05842559,  0.94212934,  0.33011931, -0.40],
  [ 0,          0,         0,          1,        ]
])
REST_COORD_UP = np.array([
  [-0.17103305,  0.31634818, -0.93309781,  0.33488534],
  [-0.98353147, -0.1109781,   0.14265242, -0.29761366],
  [-0.05842559,  0.94212934,  0.33011931, -0.3],
  [ 0,          0,         0,          1,        ]
])
fixed_z = -0.33


"""
funtion to get the new data from the screen subscriber
@param x, y : pixel coordinates of the last pressed position on the screen
"""
def new_coordinates(pos, x, y): 
  print("positions = ", pos)
  pos.append(x)
  pos.append(y)
  print("new positions = ", pos)
  print("last two elems : " , pos[-2:])

"""
"custom" goto function with added inverse kinematics to avoid rewriting the same code over and over
@param goal_coord : array with the x and y goal coordinates in reachy's coordinates
"""
def joint_goto(goal, z):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(np.array([[0, 0, -1, goal[0]],[0, 1, 0, goal[1]],[1, 0, 0, z], [0, 0, 0, 1]])))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )

def joint_goto_1(goal_coord):
  goto(
    {joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), reachy.r_arm.inverse_kinematics(goal_coord))},
    duration=2.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
  )




def main(args=None):
  #turn off to ensure compliancy before calibration
  curr_coords = [0, 0]
  reachy.turn_off_smoothly('reachy')
  while(True):
    new_coords = positions[-2:]
    if(curr_coords != new_coords):
      reachy.turn_on('reachy')
      joint_goto_1(REST_COORD)
      joint_goto_1(REST_COORD_UP)
      joint_goto(new_coords, fixed_z + 0.2)
      joint_goto(new_coords, fixed_z)
      joint_goto(new_coords, fixed_z + 0.2)
      joint_goto_1(REST_COORD_UP)
      joint_goto_1(REST_COORD)
      reachy.turn_off_smoothly('reachy')
      curr_coords = new_coords
    reachy.turn_off_smoothly('reachy')

  '''
  #screen calibration
  calibrator = Screen_Calibrator()
  calibrator.calibrate_screen(reachy, positions)
  
  #if screen not flat
  if calibrator.flat == True :
    #inititialising the processing of the screen
    processor = Screen_Processing(calibrator.screen, calibrator.fixed_z)
    print("Calibrated screen size", calibrator.screen)

    #TODO : fix this with the destination goal + recieve info from screen
    reachy.turn_on('r_arm')
    joint_goto_1(REST_COORD)
    for i in range(3):
      if i==0 :
        new_coords = [0., 0.]
      elif i==1 :
        new_coords = [0, 2000.]
      else : 
        new_coords = [2000., 0.]

      goal_coords = processor.rescale_destination_pixels_to_meters(new_coords)
      goal_coords = processor.rescale_destination_to_calibration(goal_coords, calibrator.trans_mat_1, calibrator.inverted_rot_mat)
      print("goal_coords : ", goal_coords)
      #goal_matrix = vector_to_quaternion(goal_coords, calibrator.fixed_z)
      #print("goal_mat : ", goal_matrix)
      #joint_goto(goal_coords, calibrator.fixed_z)
      #time.sleep(1.0)
      #joint_goto_1(REST_COORD)
      #time.sleep(1.0)
  
    reachy.turn_off_smoothly('reachy')

  

    print("Goal quaternion : ", goal_matrix)
    while("screen_subscriber = true"):
      if(new_coords != goal_coords):
        goal_coords = processor.rescale_destination_pixels_to_meters(new_coords)
        goal_coords = processor.rescale_destination_to_calibration(goal_coords, calibrator[2], calibrator[3], calibrator[4])
        goal_matrix = processor.vector_to_matrix_press(goal_coords)
        #reachy.turn_on('reachy')
        #joint_goto(REST_COORD)
        #joint_goto(goal_coords)
        #time.sleep(1.0)
        #joint_goto(REST_COORD)
        reachy.turn_off_smoothly('reachy')
  '''

if __name__ == '__main__':
    main()