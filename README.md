# Differential Drive Autonomous Robot (DDAR)

A ROS2 Humble + Gazebo + RViz2 simulation of a differential drive robot.

## Features
- Custom URDF robot model with base, wheels and caster
- Differential drive motion control via cmd_vel
- Odometry publishing
- Full TF tree: odom → base_link → wheels
- Synchronized Gazebo and RViz2 visualization
- LiDAR sensor with 360 degree scanning and object detection

## Requirements
- ROS2 Humble
- Gazebo Classic
- Ubuntu 22.04

## How to Run

Terminal 1 - Start Gazebo:
```bash
ros2 launch gazebo_ros gazebo.launch.py
```

Terminal 2 - Spawn robot:
```bash
ros2 run gazebo_ros spawn_entity.py -file urdf/robot.urdf -entity diff_drive_robot
```

Terminal 3 - Start RViz:
```bash
ros2 launch DDAR display.launch.py
```

Terminal 4 - Teleop:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
