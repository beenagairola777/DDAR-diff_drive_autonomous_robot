import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_dir=get_package_share_directory("DDAR")
    slam_config =os.path.join(pkg_dir,'config','slam_toolbox.yaml')
    
    
    return LaunchDescription(
    [
    Node(
    package='slam_toolbox',
    executable= 'async_slam_toolbox_node',
    name='slam_toolbox',
    output='screen',
    parameters=[slam_config, {'use_sim_time': True} ]
    
    ),
    ])
