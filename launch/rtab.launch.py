from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node
import os
import xacro


def generate_launch_description():
	
    rtabmap = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([get_package_share_directory('rtabmap_launch'), 'launch', 'rtabmap.launch.py'])
        ]),
        launch_arguments = {'frame_id':'camera_link', 'approx_sync':'true', 'rgb_topic':'/camera/color/image_raw', 'depth_topic':'/camera/aligned_depth_to_color/image_raw', 'subscribe_scan': 'false', 'visual_odometry':'true', 'camera_info_topic':'/camera/color/camera_info', 'scan_cloud_assembling':'true', 'queue_size':'20                                                            ', 'use_sime_time':'false', 'rtabmap_viz':'true','rviz':'false', 'args':'--delete_db_on_start'}.items(),
    )
    
    realsense = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                get_package_share_directory('realsense2_camera'), 'launch', 'rs_launch.py'])
            ]),
        launch_arguments={'enable_rgbd': 'true', 'enable_sync': 'true', 'align_depth.enable': 'true', 'enable_color': 'true', 'enable_depth': 'true', 'use_sim_time':'false'}.items()
    )
    
    ai = Node(
    	package="3D_Scanning_Ecommerce",
        executable="open3d",
        name='ai',
        output='screen',
    )
     
    return LaunchDescription([realsense,rtabmap,ai])
