import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

# this is the function launch  system will look for
def generate_launch_description():

    ####### DATA INPUT ##########
    urdf_file = 'robot.urdf'
    package_description = "quadruped_description"

    ####### DATA INPUT END ##########
    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "quadruped", urdf_file)
    
    # Run xacro at launch and force the result to be treated as a string
    robot_description_content = Command(['xacro ', robot_desc_path])
    robot_description = ParameterValue(robot_description_content, value_type=str)


    # Robot State Publisher

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        emulate_tty=True,
        parameters=[{'use_sim_time': True, 'robot_description': robot_description}],
        output="screen"
    )


    # create and return launch description object
    return LaunchDescription(
        [            
            robot_state_publisher_node,
        ]
    )