# Panda Color Detection and Pick-and-Place

A ROS 2 college project for detecting red, green, and blue objects and sorting them with the Franka Panda arm.

## Overview

The system uses a simulated camera feed to detect colored objects, chooses a target based on the selected color, and executes a pick-and-place motion sequence with MoveIt 2.

## Tech Stack

- ROS 2 Humble
- OpenCV
- MoveIt 2
- Gazebo
- PyMoveIt2

## Features

- Red, green, and blue object detection
- Automated pick-and-place workflow
- MoveIt 2 motion planning
- Gazebo-based simulation
- Modular ROS 2 package structure
- Docker support for repeatable setup

## Packages

- `panda_description` - robot model, worlds, and simulation assets
- `panda_controller` - control logic for the arm and gripper
- `panda_moveit` - MoveIt 2 configuration and launch files
- `panda_vision` - color detection node
- `panda_bringup` - top-level launch package
- `pymoveit2` - third-party Python MoveIt 2 interface used by the project

## Build

```bash
cd ~/panda_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Run

```bash
source install/setup.bash
ros2 launch panda_bringup pick_and_place.launch.py
```

If needed, run the pick-and-place node from another terminal after sourcing the workspace.

## Docker

Build the image from the local repository:

```bash
docker build -t panda-color-sorter -f src/Dockerfile src
```

Then launch the container with GUI support enabled for RViz and Gazebo.

## Notes

- This repository uses open-source ROS 2 packages and simulation assets.
- For a college submission, include a short summary of your own additions, testing, and integration work.

## Credits

- Franka Emika Panda
- ROS 2
- MoveIt 2
- PyMoveIt2
- OpenCV