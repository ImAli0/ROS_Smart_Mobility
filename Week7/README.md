# Application Description
## Project Overview
The project aims to demonstrate a ROS 2 application for performing computer vision tasks using an action server-
client paradigm. The action server will perform a simple image processing task, such as edge detection, and the
client will request the server to process an image.
### Nodes
1. SM_action_image_processor_server.cpp: Action server node that processes images and performs edge
detection.
2. SM_image_processor_client.cpp: Action client node that sends image processing requests to the server.
# Interaction Diagram:
![image](https://github.com/ImAli0/ROS_Smart_Mobility_Course_activities/assets/113502495/306a6e58-ce52-47f8-99dd-88a0e4c1aeb4)
## File Structure
```
ros2_cv_action_project/
│-- src/
│   |-- image_processor_server.cpp
│   |-- image_processor_client.cpp
│-- CMakeLists.txt
│-- package.xml
│-- README.md
```
# Build the Project
```
colcon build --packages-select ros2_cv_action_project
```
# Running the Project
### Starting the Action Server
```
ros2 run ros2_cv_action_project image_processor_server
```
### Sending a request with the action client
```
ros2 run ros2_cv_action_project image_processor_client
```
Feel free to expand on this README with more specific details and guidelines to suit your project's needs.
