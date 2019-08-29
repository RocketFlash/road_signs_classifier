cmake_minimum_required(VERSION 2.8.3)
project(road_signs_classifier)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  geometry_msgs
  message_generation
  rospy
  std_msgs
  roslib
  detection_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime geometry_msgs rospy sensor_msgs std_msgs detection_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
