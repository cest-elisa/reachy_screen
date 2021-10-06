# Screen App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A simple application to monitor mouse (inc. touch) events via ROS.


### License

The whole package is under MIT License, see [LICENSE](LICENSE).

This README is based on the project [ros_best_practices](https://github.com/leggedrobotics/ros_best_practices), Copyright 2015-2017, Péter Fankhauser. It is licensed under the BSD 3-Clause Clear License. See [doc/LICENSE](doc/LICENSE) for additional details.

**Author: Utku Norman<br />
Affiliation: [CHILI Lab, EPFL](https://www.epfl.ch/labs/chili/)<br />
Maintainer: Utku Norman, utku.norman@epfl.ch**

The [justhink_scenario] package has been tested under [ROS] Noetic on Ubuntu 20.04.
This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.


## Installation

### Building from Source

#### Dependencies

* [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics) for the communication between this ([justhink_scenario]) application's node and the robot behaviour node from [justhink_robot]


#### Building

1) [Install ROS Noetic](http://wiki.ros.org/Installation/).

2) [Create a ROS workspace for catkin](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) (e.g. `~/catkin_ws`):
```
# Load the default workspace.
source /opt/ros/noetic/setup.bash

# Create and overlay your catkin workspace.
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
source devel/setup.bash
```

3) Build this package with ROS (this also installs the justhink_scenario Python package):
```
cd ~/catkin_ws
catkin build screen_app
source devel/setup.bash
```

If you receive an error `catkin: not found`, make sure you have sourced the ROS environment (i.e. `source ~/catkin_ws/devel/setup.bash` and `source /opt/ros/noetic/setup.bash`), and you have installed the catkin tools by `sudo apt-get install python-catkin-tools`.

4) Check the installation by running the following in a Python interpreter:
```
from screen_app import show_app
```


## Usage

1) In a terminal, start the 'roscore':
```
roscore
```

2) In another terminal, run the main node with:
```
rosrun screen_app run_app.py
```

### Running with a touch screen

#### Mapping the touch interface onto the touch screen

Check the name of the touch controller. With iiyama, it is "USBest Technology SiS HID Touch Controller"
```
xinput
```

2) Check the name of the screen, e.g. in mine it is "DP-3"
```
xrandr -q
```

3) Map the touch controller to the screen, e.g., if it is DP-3 from the previous step:
```
xinput map-to-output "USBest Technology SiS HID Touch Controller" DP-3
```

#### Hiding the cursor on touch events

Install the fork of unclutter that hides the cursor for touch only (The default unclutter from apt does not have "-touch".)
```
sudo apt install asciidoc libev-dev libxslt1-dev docbook-xsl xsltproc libxml2-utils    # Prerequisites
git clone https://github.com/nowrep/unclutter-xfixes.git
cd unclutter-xfixes
make
sudo make install
```

5) Run unclutter on a separate terminal. Touch on the screen will not show cursor.
```
unclutter -touch
```

#### Rotating the screen by 180 degrees
To prevent the power button being pressed accidentally (normally bottom right corner, if rotated top left corner)

1) In Display setting of Ubuntu, change Rotation to 180 degrees.

2) Remap the touch upside-down.
```
xinput set-prop "USBest Technology SiS HID Touch Controller" --type=float "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
```



## Nodes

### screen_app

Launches a simple application to monitor mouse and key events.

The ROS computation graph (as visualised by [rqt_graph](http://wiki.ros.org/rqt_graph)) is as follows:


![](doc/rosgraph.png)

#### Subscribed Topics

None.


#### Published Topics

* **`mouse_press`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse clicks that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name, for logging purposes.

* **`mouse_drag`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse drags that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name, for logging purposes.

* **`mouse_release`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse releases that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name, for logging purposes.

* **`mouse_motion`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse movements that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name, for logging purposes.

* **`key_press`** ([[screen_app/Key]](https://github.com/utku-norman/screen_app/blob/main/msg/Key.msg))

	Key presses on the keyboard that have the symbol and modifiers information, for logging purposes.

* **`key_release`** ([[screen_app/Key]](https://github.com/utku-norman/screen_app/blob/main/msg/Key.msg))

	Key releases on the keyboard that have the symbol and modifiers information, for logging purposes.