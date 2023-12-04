import rclpy
from rclpy.action import ActionClient

from fleet_management_py.action import FleetManagement

def fleet_management_client():
    rclpy.init()
    client = ActionClient('/fleet_management', FleetManagement)

    goal_msg = FleetManagement.Goal()
    goal_msg.fleet_size = 5  # Set the desired fleet size here

    client.wait_for_server()

    future = client.send_goal_async(goal_msg)

    rclpy.spin_until_future_complete(rclpy.context, future)

    if future.result() is not None:
        result = future.result().result.routes
        print("Received routes:")
        for i, route in enumerate(result):
            print(f"Route {i + 1}: {route}")
    else:
        print("Action failed to complete")

    rclpy.shutdown()

if __name__ == '__main__':
    fleet_management_client()

