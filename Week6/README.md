# Enabling Topic Statistics (Advanced)

This README provides instructions on how to set up and run a ROS 2 C++ subscriber with topic statistics in the `cpp_pubsub` package. This allows you to enable topic statistics for a subscriber node, view the statistics data, and analyze the performance of your ROS 2 system.

## Prerequisites

- ROS 2 installed on your system.
- A workspace with the `cpp_pubsub` package (from the ROS 2 tutorials).

## Instructions

1. **Navigate to the `cpp_pubsub` Package Directory:**

   ```
   cd ~/ros2_ws/src/cpp_pubsub
   ```

    Download the Example Code with Topic Statistics:

    Download the example subscriber code with topic statistics:

    ```
    wget -O src/member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/humble/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/586f8b7c-2f4b-49e4-a37b-1da9bca77b37)

Modify CMakeLists.txt:

Add the new executable listener_with_topic_statistics to the CMakeLists.txt file. This allows you to build the subscriber with topic statistics:

```
cat <<EOL >> CMakeLists.txt
# Add the listener_with_topic_statistics executable
add_executable(listener_with_topic_statistics src/member_function_with_topic_statistics.cpp)
ament_target_dependencies(listener_with_topic_statistics rclcpp std_msgs)

install(TARGETS
  talker
  listener
  listener_with_topic_statistics
  DESTINATION lib/\${PROJECT_NAME})
EOL
```
Modify package.xml:

Add dependencies for rclcpp and std_msgs in the package.xml file:
```
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:build_depend" -t elem -v "rclcpp" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:build_depend" -t elem -v "std_msgs" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:exec_depend" -t elem -v "rclcpp" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:exec_depend" -t elem -v "std_msgs" package.xml
```
Build the ROS 2 Workspace:

Build your ROS 2 workspace to include the new listener_with_topic_statistics executable:
```
cd ~/ros2_ws
colcon build --symlink-install
```
Run the Subscriber with Topic Statistics:

Run the subscriber with topic statistics enabled:
```
ros2 run cpp_pubsub listener_with_topic_statistics
```
Run the Talker Node:

Open a new terminal and run the talker node (optionally, you can run this in the background):
```
ros2 run cpp_pubsub talker
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/15b7da62-fbf4-484e-97b8-9a811cfcbc89)

View Available Topics:

In a new terminal, you can view the available topics:
```
ros2 topic list
```
Observe Published Statistics Data:

To observe the published statistics data, use the following command:
```
ros2 topic echo /statistics
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/3a87caa6-cd81-4606-8e69-d3f4e6ef1e8d)

The terminal will start displaying statistics messages every 10 seconds, as specified in the code.
