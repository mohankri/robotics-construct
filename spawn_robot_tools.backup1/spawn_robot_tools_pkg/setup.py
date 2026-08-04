from setuptools import setup
import os
from glob import glob

package_name = 'spawn_robot_tools_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tgrip',
    maintainer_email='duckfrost@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'inertia_wizzard = spawn_robot_tools_pkg.inertia_calculator_node:main',
            'robot_description_publisher_exe = spawn_robot_tools_pkg.robot_description_publisher:main'
        ],
    },
)
