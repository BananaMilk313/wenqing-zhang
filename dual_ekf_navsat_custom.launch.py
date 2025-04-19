from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node_odom',
            output='screen',
            parameters=['../params/dual_ekf_navsat_custom.yaml'],
            remappings=[
                ('odometry/filtered', 'odometry/filtered_odom')
            ]
        ),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node_map',
            output='screen',
            parameters=['../params/dual_ekf_navsat_custom.yaml'],
            remappings=[
                ('odometry/filtered', 'odometry/filtered_map')
            ]
        ),
        Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform',
            output='screen',
            parameters=['../params/dual_ekf_navsat_custom.yaml'],
            remappings=[
                ('imu', '/imu'),
                ('gps/fix', '/fix'),
                ('gps/filtered', '/gps/filtered'),
                ('odometry/gps', '/odometry/gps'),
                ('odometry/filtered', '/odometry/filtered_map')
            ]
        )
    ])




