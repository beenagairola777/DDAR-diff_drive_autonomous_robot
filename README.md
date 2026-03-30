# Differential Drive Autonomous Robot (DDAR)

A ROS2 Humble simulation of a differential drive robot with autonomous navigation using Nav2 and SLAM Toolbox.

## Project Phases

- ✅ Phase 1 — Robot simulation (URDF, Gazebo, RViz2)
- ✅ Phase 2 — SLAM mapping (SLAM Toolbox, map saved)
- ✅ Phase 3 — Autonomous navigation (Nav2, AMCL, obstacle avoidance)

## Features

- Custom URDF differential drive robot with LiDAR (360°, 0.2–10m range)
- Gazebo Classic simulation with obstacle world
- SLAM Toolbox for map generation
- Nav2 stack with AMCL localization
- DWB local planner for obstacle avoidance
- Autonomous goal navigation via RViz2 or command line

## Requirements

- ROS2 Humble
- Gazebo Classic
- Ubuntu 22.04 (VirtualBox compatible)
- Nav2, SLAM Toolbox packages

## How to Run

**Terminal 1 — Gazebo:**
```bash
cd ~/ros2_ar && source install/setup.bash
ros2 launch DDAR gazebo.launch.py
```

**Terminal 2 — Nav2 (after Gazebo stable):**
```bash
cd ~/ros2_ar && source install/setup.bash
ros2 launch DDAR nav2.launch.py
```

**Terminal 3 — RViz2:**
```bash
rviz2 -d ~/ros2_ar/src/DDAR/rviz/slam_view.rviz
```

**Terminal 4 — Set Initial Pose (required every session):**
```bash
ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped "{header: {frame_id: 'map'}, pose: {pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}}, covariance: [0.25,0,0,0,0,0, 0,0.25,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0.06853]}}"
```

## RViz2 Setup (each session)

1. Fixed Frame → `map`
2. Add Map display → Topic `/map` → Durability Policy → `Transient Local`

## Send Navigation Goal

**Via RViz2:** Use `2D Goal Pose` button on toolbar

**Via command line:**
```bash
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{pose: {header: {frame_id: 'map'}, pose: {position: {x: 2.0, y: 1.0, z: 0.0}, orientation: {w: 1.0}}}}"
```

## World Obstacles

| Obstacle | Type | Position |
|----------|------|----------|
| box_obstacle_1 | Box (0.5x0.5) | x=2, y=2 |
| box_obstacle_2 | Box (0.5x0.5) | x=-2, y=-2 |
| cylinder_obstacle | Cylinder (r=0.3) | x=-2, y=3 |

## Known Limitations

- Initial pose must be set manually every session (AMCL requirement)
- RViz2 costmap appears yellow in VirtualBox due to graphics limitations — navigation works correctly
- Real hardware deployment will not have these visualization issues

## Author

Beena Gairola  
GitHub: github.com/beenagairola777  
M.Tech Robotics Engineering, UPES Dehradun
