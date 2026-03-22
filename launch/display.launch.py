import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory  # FIX 7: proper path


def generate_launch_description():

    # FIX 7: use ament index instead of hardcoded HOME path
    # Replace 'DDAR' with your actual ROS2 package name
    pkg_dir = get_package_share_directory('DDAR')
    urdf_file = os.path.join(pkg_dir, 'urdf', 'robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[
                {'robot_description': robot_desc},
                {'use_sim_time': True},   # correct — kept from your file
            ],                             # FIX 5: was missing the closing ]
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            # FIX 6: added use_sim_time — without this RViz rejects all TF data
            parameters=[{'use_sim_time': True}],
            output='screen'
        ),

    ])
