cmake_minimum_required(VERSION 2.8.3)
project(road_signs_classifier)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  geometry_msgs
  message_generation
  cv_bridge
  rospy
  std_msgs
  roslib
  detection_msgs
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
