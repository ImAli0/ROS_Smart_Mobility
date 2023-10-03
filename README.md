# ROS 2 C++ Subscriber with Topic Statistics

This README provides instructions on how to set up and run a ROS 2 C++ subscriber with topic statistics in the `cpp_pubsub` package. This allows you to enable topic statistics for a subscriber node, view the statistics data, and analyze the performance of your ROS 2 system.

## Prerequisites

- ROS 2 installed on your system.
- A workspace with the `cpp_pubsub` package (from the ROS 2 tutorials).

## Instructions

1. **Navigate to the `cpp_pubsub` Package Directory:**

   ```bash
   cd ~/ros2_ws/src/cpp_pubsub

    Download the Example Code with Topic Statistics:

    Download the example subscriber code with topic statistics:

    bash

wget -O src/member_function_with_topic_statistics.cpp https://raw.githubusercontent.com/ros2/examples/humble/rclcpp/topics/minimal_subscriber/member_function_with_topic_statistics.cpp

Modify CMakeLists.txt:

Add the new executable listener_with_topic_statistics to the CMakeLists.txt file. This allows you to build the subscriber with topic statistics:

bash

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

Modify package.xml:

Add dependencies for rclcpp and std_msgs in the package.xml file:

bash

xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:build_depend" -t elem -v "rclcpp" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:build_depend" -t elem -v "std_msgs" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:exec_depend" -t elem -v "rclcpp" package.xml
xmlstarlet edit --inplace -N x="http://www.w3.org/1999/XML" -s "/x:package/x:exec_depend" -t elem -v "std_msgs" package.xml

Build the ROS 2 Workspace:

Build your ROS 2 workspace to include the new listener_with_topic_statistics executable:

bash

cd ~/ros2_ws
colcon build --symlink-install

Run the Subscriber with Topic Statistics:

Run the subscriber with topic statistics enabled:

bash

ros2 run cpp_pubsub listener_with_topic_statistics

Run the Talker Node:

Open a new terminal and run the talker node (optionally, you can run this in the background):

bash

ros2 run cpp_pubsub talker

View Available Topics:

In a new terminal, you can view the available topics:

bash

ros2 topic list

Observe Published Statistics Data:

To observe the published statistics data, use the following command:

bash

ros2 topic echo /statistics

The terminal will start displaying statistics messages every 10 seconds, as specified in the code.
