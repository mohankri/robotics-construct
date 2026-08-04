import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

import xacro

import launch

# this is the function launch  system will look for
def generate_launch_description():
    
    ####### DATA INPUT ##########
    urdf_file = 'camera_bot.urdf'
    #xacro_file = "box_bot.xacro"
    package_description = "turtle_tf_3d_ros2"

    ####### DATA INPUT END ##########
    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "urdf", urdf_file)

    robot_desc = xacro.process_file(robot_desc_path)
    xml = robot_desc.toxml()

    
    # Publish Robot Desciption in String form in the topic /robot_description
    publish_robot_description = Node(
        package="spawn_robot_tools_pkg",
        executable='robot_description_publisher_exe',
        name='cam_bot_robot_description_publisher',
        output='screen',
        emulate_tty=True,
        arguments=['-xml_string', xml,
                   '-robot_description_topic', '/cam_bot_robot_description'
                   ]
    )

    # Robot State Publisher
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='cam_bot_robot_state_publisher',
        emulate_tty=True,
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': xml}],
        remappings=[("/robot_description", "/cam_bot_robot_description")
        ],
        output="screen"
    )

    # RVIZ Configuration
    rviz_config_dir = os.path.join(get_package_share_directory(package_description), 'rviz', 'gazebo_vis.rviz')


    rviz_node = Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            name='rviz_node',
            emulate_tty=True,
            parameters=[{'use_sim_time': True}],
            arguments=['-d', rviz_config_dir])

    # create and return launch description object
    return LaunchDescription(
        [            
            publish_robot_description,
            robot_state_publisher_node,
        ]
    )
