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

# Using Fast DDS Discovery Server as discovery protocol
## Running the Talker-Listener ROS 2 Demo
The talker-listener ROS 2 demo consists of a talker node that publishes a "hello world" message every second and a listener node that subscribes to these messages. To set up and run this demo, follow the steps below.
## Setup Discovery Server
Start by launching a discovery server with id 0, default port 11811, and listening on all available interfaces. Open a new terminal and run:
    
```
fastdds discovery --server-id 0
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/a9ddbaa3-c215-49ce-b218-3696670008ac)

## Launch Listener Node
Execute the listener demo, which listens to the /chatter topic. In a new terminal, set the environment variable ROS_DISCOVERY_SERVER to the location of the discovery server. Ensure you've sourced ROS 2 in every new terminal:
```
export ROS_DISCOVERY_SERVER=127.0.0.1:11811
ros2 run demo_nodes_cpp listener --ros-args --remap __node:=listener_discovery_server
```
This command will create a ROS 2 node that automatically creates a client for the discovery server to perform discovery.

## Launch Talker Node

Open a new terminal and set the ROS_DISCOVERY_SERVER environment variable as before to enable the node to start a discovery client:

```
export ROS_DISCOVERY_SERVER=127.0.0.1:11811
ros2 run demo_nodes_cpp talker --ros-args --remap __node:=talker_discovery_server
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/42d1f213-1175-4834-91ad-82ad94d23802)

You should now see the talker node publishing "hello world" messages, and the listener node receiving these messages.

## Demonstrate Discovery Server Execution
To demonstrate that the Discovery Server is working differently from the standard talker-listener example, run another node that is not connected to the discovery server. Start a new listener (listening on the /chatter topic by default) in a new terminal and check that it is not connected to the talker already running:
```
ros2 run demo_nodes_cpp listener --ros-args --remap __node:=simple_listener
```
The new listener node should not be receiving the "hello world" messages.

Finally, create a new talker using the simple discovery protocol (the default DDS distributed discovery mechanism) for discovery:
```
ros2 run demo_nodes_cpp talker --ros-args --remap __node:=simple_talker
```
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/7973e997-32ae-4f2a-9cbc-956a365b2b28)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/8ae077ef-a731-4d86-99da-f415cf2f2842)

Now, you should see the simple_listener node receiving "hello world" messages from simple_talker but not from talker_discovery_server.

## Visualization Tool rqt_graph

The rqt_graph tool can be used to verify the nodes and structure of this example. To see the listener_discovery_server and talker_discovery_server nodes, set the ROS_DISCOVERY_SERVER environment variable before launching it.
## Advanced Use Cases

The following sections explore advanced features of the Discovery Server to create more robust network configurations and optimize ROS 2 introspection tools.
### Server Redundancy

By using the fastdds tool, multiple discovery servers can be created. Discovery clients (ROS nodes) can connect to as many servers as desired, allowing for a redundant network that remains functional even if some servers or nodes shut down unexpectedly.
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/2649e20a-ffe3-49b9-bf99-4a942a7d9be6)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/6aa4a103-ed2f-4722-b393-23a7f79a1c92)

### Backup Server

The Fast DDS Discovery Server supports creating a server with backup functionality. This allows the server to restore its last state in case of a shutdown, preventing the need for a complete rediscovery process and data loss.
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/866a117f-f919-4dd8-acf1-75a276821aac)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/82f105f9-5910-4846-a84d-c0b8ec276d89)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/6034ff44-7927-4858-8ea1-23c77c426e36)

### Discovery Partitions

Communication with discovery servers can be split to create virtual partitions in the discovery information. This means that two endpoints will only know about each other if there is a shared discovery server or a network of discovery servers between them.
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/53e398ec-27f0-4967-a352-2c0db2e03ef1)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/fa6b940e-8009-4731-ad76-09169a861977)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/fdcccf00-9b1d-48bb-9db6-3ddca6bce885)
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/c5ddd9b2-6f2a-4c12-b5f7-393c712f31fa)

### ROS 2 Introspection

The ROS 2 Command Line Interface supports introspection tools to analyze the behavior of a ROS 2 network. Some tools, like ros2 bag record, ros2 topic list, and more, benefit from the Discovery Server's capabilities. This section explains how to configure ROS 2 introspection tools to work effectively with the Discovery Server.
Daemon's Related Tools

The ROS 2 Daemon is used in several ROS 2 CLI introspection tools. To use these tools with the Discovery Server mechanism, configure the ROS 2 Daemon as a Super Client.
No Daemon Tools

Some ROS 2 CLI tools do not use the ROS 2 Daemon. To connect these tools with a Discovery Server and receive all topics' information, instantiate them as Super Clients.
### Compare Fast DDS Discovery Server with Simple Discovery Protocol

For advanced users who wish to compare nodes running with the Discovery Server against the default Simple Discovery Protocol, scripts are provided to generate network traffic traces and graphs. These scripts require tshark to be installed on your system.

For detailed instructions on running these comparisons, refer to the respective sections in the documentation.

These advanced features and scenarios demonstrate the power and flexibility of the ROS 2 Discovery Server for managing and optimizing ROS 2 network communication.
