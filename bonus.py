from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='q2',
            node_namespace='q2_sservice',
            node_executable='q2_service_node',
            node_name='service'
        ),
        Node(
            package='q2',
            node_namespace='q2_client',
            node_executable='q2_client_node',
            node_name='client'
        ),
        Node(
            package='q2',
            node_executable='q2_',
            node_name='mimic',
            remappings=[
                ('/input/pose', '/camera/rgb')
            ]
        )
    ])