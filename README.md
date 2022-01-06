# Reachy touchscreen interaction project

To utilize this project, copy the contents of `reachy_screen\reachy_screen\..` into Utku Norman's `screen_app\screen_app\...` then run ``screen_app\run_app.py`` according to his README, as well as ``JUSThink_node\intended_points.py`` according to its README. 

Once it all the previous files are running, run ``screen_app\screen_subscriber.py``.  

​	

`reachy_screen\screen\screen_info.py` : file with a class defining the screen. Contains all the information regarding the screen currently in use. Only predefined parameters : screen's resolution (= screen size in pixels)

`reachy_screen\screen_subscriber.py` : subscribes to run_app's `mouse_press` topic, as well as JUSThink's `intended_points` topic. Depending on the current stage (screen calibrated or not), either calls for the calibration through `screen\screen_getpoints.py`, or for Reachy to press a point through `screen\screen_touch.py` 

​	

##  Step 1 : Screen Calibration 

This part contains the details of the implementation for the calibration of the touchscreen. 

It is comprised of three main python files: `screen\screen_calibration.py`,  `screen\screen_getpoints.py` and `screen\screen_new_trilateration.py`

`screen\screen_getpoints.py` : allows to gather points simultaneously from the screen and Reachy, using respectively Utku's screen_app publisher and Pollen Robotics' forward kinematics function. Also ensures that two calibrated points are not too close together, or pressing by accident twice on the same point. Once it gets three distinct points (A, B and C), calls `screen_calibration` 

`screen\screen_calibration.py` : extracts data from A, B and C to : check if the screen is laying flat on a surface ; update the `screen_info` screen's pixel_size and screen_size ; computes the screens' coordinate axis ; compute the translation and rotation matrix from Reachy to the screen and vice-versa ; calls `screen_new_trilateration`

`screen\screen_new_trilateration.py` : trilaterates the Reachy coordinates of a given destination point from the three calibration points A, B and C by computing the three-circle intersection. 

 	


##  Step 2 : Data Processing

`screen\screen_processing.py` : processes every given point from the screen's (x, y) pixel coordinates to Reachy's (x, y) meter coordinates. Does this by adjusting according to the screen's pixel_size, and the translation and rotation matrices. Also checks if the given point is actually inside of the screen's bounds. 

​	

## Step 3 : Screen Interaction 

`screen\screen_touch.py` : turns Reachy's right arm on, extracts of all the destinations points from the array, calls `screen_processing.py` to adapt them and proceeds to do the three-step process to make Reachy press the screen. 

​	



## Testing : 

All of the data for the accuracy and precision testing is available in `reachy_screen/testing_results`



## Calculations : 

Contains the hand-written notes for the reasoning behind the calibration and processing steps of the project. Available in `reachy_screen/calculations`



## Video demonstrations:

Contains the final video demonstration of Reachy's capabilities : the calibration step, game interaction with JUSThink, and a test to make Reachy copy the user's presses. Available in `reachy_screen/video_demo`