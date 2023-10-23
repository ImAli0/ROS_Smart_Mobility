# Fleet Management ROS 2 Package


## Overview

The Fleet Management ROS 2 package is designed to manage and allocate vehicles for various applications. This README provides an overview of the project, installation instructions, usage examples, and test scenarios.

### Use Cases

The fleet management package is suitable for a variety of use cases, including:

- Local delivery services
- Ride-sharing platforms
- Logistics and transportation companies
- Emergency services



# Navigate to your ROS 2 workspace
```
cd ~/ros2_ws
```
```
# Build the package
colcon build

# Source the workspace
source install/setup.bash
```
## Usage
Action Server

The package includes an Action Server for fleet management. The server can be started as follows:

``` 
ros2 run fleet_management fleet_management_server_cli.py
```

## Action Client

You can use the Action Client to request fleet management tasks by specifying the fleet size. It sends a request to the server and displays the calculated routes.

```
ros2 run fleet_management fleet_management_client_cli.py allocate_route <fleet_size>
```

Replace <fleet_size> with the desired fleet size.
Command Line Interface (CLI)

For a user-friendly CLI that allows users to allocate and route vehicles, use the following command:

```
./fleet_management_cli.py allocate_route <fleet_size>
```

## Launch Files

You can run the entire fleet management system using the provided launch file. Make sure the launch file is located in the launch directory of your package:

```
ros2 launch fleet_management fleet_management_launch.py
```
## Test Scenarios

Here are two test scenarios with expected output:

Scenario 1: Local Delivery Service

 Fleet Size: 10 vehicles

Expected Output: Vehicle routes optimized for local deliveries.
    Goal Description: Your goal is to manage a local delivery service with a fleet of vehicles. You want to allocate and route vehicles for delivering packages to customers within a city.

Fleet Size: 10 vehicles

Expected Output (Vehicle Routes):

        Vehicle 1: Start at the warehouse, deliver to Customer A, Customer B, and return to the warehouse.
        
        Vehicle 2: Start at the warehouse, deliver to Customer C, Customer D, and return to the warehouse.
        
        Vehicle 3: Start at the warehouse, deliver to Customer E, Customer F, and return to the warehouse.
        
        Vehicle 4: Start at the warehouse, deliver to Customer G, Customer H, and return to the warehouse.
        
        Vehicle 5: Start at the warehouse, deliver to Customer I, Customer J, and return to the warehouse.
        
        Vehicle 6: Start at the warehouse, deliver to Customer K, Customer L, and return to the warehouse.
        
        Vehicle 7: Start at the warehouse, deliver to Customer M, Customer N, and return to the warehouse.
        
        Vehicle 8: Start at the warehouse, deliver to Customer O, Customer P, and return to the warehouse.
        
        Vehicle 9: Start at the warehouse, deliver to Customer Q, Customer R, and return to the warehouse.
        
        Vehicle 10: Start at the warehouse, deliver to Customer S, Customer T, and return to the warehouse.
        

Scenario 2: Ride-Sharing Service

Fleet Size: 5 vehicles

Expected Output: Routes optimized for ride-sharing services.
    Goal Description: You are managing a ride-sharing service in a busy urban area. Your goal is to allocate and route vehicles to pick up passengers and drop them off at their destinations efficiently.


Expected Output (Vehicle Routes):

        Vehicle 1: Start at the central hub, pick up Passenger A, drop off at Location X, and return to the central hub.
        
        Vehicle 2: Start at the central hub, pick up Passenger B, drop off at Location Y, and return to the central hub.
        
        Vehicle 3: Start at the central hub, pick up Passenger C, drop off at Location Z, and return to the central hub.
        
        Vehicle 4: Start at the central hub, pick up Passenger D, drop off at Location W, and return to the central hub.
        
        Vehicle 5: Start at the central hub, pick up Passenger E, drop off at Location V, and return to the central hub.
        
        
In both scenarios, the expected output represents the routes that each vehicle will take to complete its tasks. The fleet management system should efficiently allocate and route the vehicles to achieve the goals described in each scenario. These scenarios can be used to test your fleet management application to ensure it performs as expected.

