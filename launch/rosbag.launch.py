from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    rviz_path = get_package_share_directory('rviz_panel_gui')
    rviz = Node(
        package='rviz2',
        namespace='',
        executable='rviz2',
        output='screen',
        arguments=['-d' + os.path.join(rviz_path, 
                    'launch', 'rosbag.rviz')]
    )

    return LaunchDescription([
        rviz,
    ])

