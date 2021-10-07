# Screen App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A simple application to monitor mouse (including touch) events via ROS 2.
Default size is 1920x1080, and the window is by default moved to the external screen: you can modify [AppWindow](screen_app/screen_app/run_app.py) to change these.

### License

The whole package is under MIT License, see [LICENSE](LICENSE).

This README is based on the project [ros_best_practices](https://github.com/leggedrobotics/ros_best_practices), Copyright 2015-2017, Péter Fankhauser. It is licensed under the BSD 3-Clause Clear License. See [doc/LICENSE](doc/LICENSE) for additional details.

**Author: Utku Norman<br />
Affiliation: [CHILI Lab, EPFL](https://www.epfl.ch/labs/chili/)<br />
Maintainer: Utku Norman, utku.norman@epfl.ch**

The [screen_app] package has been tested under [ROS] Foxy on Ubuntu 20.04.
This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.


## Installation

### Building from Source

#### Dependencies

* [Robot Operating System (ROS 2)](https://docs.ros.org) (middleware for robotics)


#### Building

1) [Install ROS Foxy](https://docs.ros.org/en/foxy/Installation.html).

2) Create a ROS workspace (e.g. `~/ros2_foxy`):
```
# Create and overlay your catkin workspace.
mkdir -p ~/ros2_foxy/src
cd ~/ros2_foxy/
source install/setup.bash
```

3) Clone this package:
```
cd ~/ros2_foxy
git clone https://github.com/utku-norman/screen_app.git
```

4) Checkout ros2 branch:
```
cd screen_app
git checkout ros2
```

5) Build this package with ROS (this also installs the justhink_scenario Python package):
```
cd ~/ros2_foxy
colcon build --symlink-install --packages-select screen_app
source install/setup.bash
```

6) Check the installation by running the following in a terminal:
```
ros2 interface show screen_app/msg/Mouse
```


## Usage

In another terminal, run the node with:
```
ros2 run screen_app run_app.py
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

Launches a simple application to monitor mouse and key events in ROS2.
Default size is 1920x1080, and the window is by default moved to the external screen.

A screenshot:
![](doc/screenshot.png)

The ROS computation graph (as visualised by [rqt_graph](http://wiki.ros.org/rqt_graph)) is as follows:


![](doc/rosgraph.png)

#### Subscribed Topics

None.


#### Published Topics

* **`mouse_motion`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse movements that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name.

* **`mouse_press`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse clicks that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name.

* **`mouse_drag`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse drags that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name.

* **`mouse_release`** ([[screen_app/Mouse]](https://github.com/utku-norman/screen_app/blob/main/msg/Mouse.msg))

	Mouse releases that have position, position difference and mouse button information, with a header that contains a timestamp and an activity name.

* **`key_press`** ([[screen_app/Key]](https://github.com/utku-norman/screen_app/blob/main/msg/Key.msg))

	Key presses on the keyboard that have the symbol and modifiers information, for logging purposes.

* **`key_release`** ([[screen_app/Key]](https://github.com/utku-norman/screen_app/blob/main/msg/Key.msg))

	Key releases on the keyboard that have the symbol and modifiers information, for logging purposes.