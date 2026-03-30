import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # Get the path to our package
    pkg_dir = get_package_share_directory('DDAR')

    # Path to our robot URDF file
    urdf_file = os.path.join(pkg_dir, 'urdf', 'robot.urdf')

    # Path to our world file
    world_file = os.path.join(pkg_dir, 'worlds', 'obstacles.world')

    # Read the URDF file contents
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([

        # 1. START GAZEBO with our world file
        # ExecuteProcess runs a terminal command — here we launch Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose',
                 '-s', 'libgazebo_ros_init.so',      # ROS2-Gazebo bridge
                 '-s', 'libgazebo_ros_factory.so',   # allows spawning robots
                  '--world', world_file],
            output='screen'
        ),

        # 2. START robot_state_publisher
        # This reads the URDF and publishes all the TF transforms
        # (tells ROS2 where each part of the robot is relative to others)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[
                {'robot_description': robot_desc},
                {'use_sim_time': True},
            ],
            output='screen'
        ),

        # 3. SPAWN the robot into Gazebo
        # This takes the URDF and places the robot at position (0, 0, 0.1)
        # x=0, y=0, z=0.1 (slightly above ground so it doesn't clip)
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_robot',
            arguments=[
                '-topic', 'robot_description',  # reads URDF from this topic
                '-entity', 'ddar_robot',         # name of robot in Gazebo
                '-x', '0', '-y', '0', '-z', '0.1'  # spawn position
            ],
            output='screen'
        ),

      
    ])
