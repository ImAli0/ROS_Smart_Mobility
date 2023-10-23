# fleet_management_py/launch/fleet_management_launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'fleet_size',
            default_value='5',  # Specify the default fleet size
            description='Desired fleet size for fleet management'
        ),
        Node(
            package='fleet_management',
            executable='fleet_management_server_cli.py',
            name='fleet_management_server',
            output='screen',
        ),
        Node(
            package='fleet_management',
            executable='fleet_management_client_cli.py',
            name='fleet_management_client',
            output='screen',
            parameters=[{'fleet_size': LaunchConfiguration('fleet_size')}],
        ),
    ])

