from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import time
import numpy as np
from screen_calibration import Screen_Calibrator
from screen_processing import Screen_Processing

#TODO : all the links with reachy (--> figure how to get position by pressing a key) 
#TODO : all the links with the screen subscriber
#TODO later : make  the head look at the head ? 
#TODO later : check the temperatures all along to avoid frying some motors
#TODO later : choose which arm moves depending on the distance from goal
#TODO later : choose if otis hand moves or the arm moves depending on distance from goal


reachy = ReachySDK(host='127.0.0.1') 
 
REST_COORD = np.array([
  [1, 0, 0, 0.1],
  [0, 1, 0, -0.2],  
  [0, 0, 1, -0.2],
  [0, 0, 0, 1],  
])

"""
funtion to get the new data from the screen subscriber
@param x, y : pixel coordinates of the last pressed position on the screen
"""
def new_coordinates(x, y): 
  new_x = x
  new_y = y
  new_coordinates = True
  print("x = ", x, "; y = ", y, "; new_coord = ", new_coordinates)


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
  reachy.turn_off_smoothly('reachy')

  #screen calibration
  calibrator = Screen_Calibrator()
  calibrator.calibrate_screen(reachy)
  
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
      goal_coords = processor.rescale_destination_to_calibration(goal_coords, calibrator.trans_mat_1, calibrator.inverted_rot_mat, calibrator.trans_mat_2)
      print("goal_coords : ", goal_coords)
      #goal_matrix = vector_to_quaternion(goal_coords, calibrator.fixed_z)
      #print("goal_mat : ", goal_matrix)
      joint_goto(goal_coords, calibrator.fixed_z)
      time.sleep(1.0)
      joint_goto_1(REST_COORD)
      time.sleep(1.0)

    reachy.turn_off_smoothly('reachy')

  '''

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