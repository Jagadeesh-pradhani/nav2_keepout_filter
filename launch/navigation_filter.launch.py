import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node




def generate_launch_description():

    curr_dir = get_package_share_directory('nav2_keepout_filter')
    launch_dir = os.path.join(get_package_share_directory('nav2_keepout_filter'), 'launch')

    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    mask_yaml_file = LaunchConfiguration('mask')
    namespace = LaunchConfiguration('namespace')
    map_dir = LaunchConfiguration('map')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value=os.path.join(
                curr_dir,
                'map',
                'turtlebot3_world.yaml'),
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params_file',
            default_value=os.path.join(
                curr_dir,
                'params',
                'mask.yaml'),
            description='Full path to param file to load'),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),
        
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Top-level namespace'),
        
        DeclareLaunchArgument(
            'mask',
            default_value=os.path.join(
                curr_dir,
                'map',
                'keepout_mask.yaml'),
            description='Full path to filter mask yaml file to load'),




        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_dir, '/filter.launch.py']),
            launch_arguments={
                'mask': mask_yaml_file,
                'use_sim_time': use_sim_time,
                'params_file': params_file,
                'namespace': namespace}.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_dir, '/navigation2.launch.py']),
            launch_arguments={
                'map': map_dir,
                'use_sim_time': use_sim_time,
                'params_file': params_file}.items(),
        ),

    ])
