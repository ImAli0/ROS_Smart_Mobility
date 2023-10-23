import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from fleet_management_py.msg import FleetSize
from fleet_management_py.action import FleetManagement

class FleetManagementServer(Node):

    def __init__(self):
        super().__init__('fleet_management_server')
        self.server = ActionServer(self, FleetManagement, 'fleet_management', self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Received request for fleet size: %d' % goal_handle.request.fleet_size)

        # Perform fleet management logic (e.g., allocation and routing)
        routes = self.calculate_routes(goal_handle.request.fleet_size)

        if routes is not None:
            result = FleetManagement.Result()
            result.routes = routes
            goal_handle.succeed(result)
            self.get_logger().info('Successfully calculated routes and sent result.')
        else:
            goal_handle.abort()
            self.get_logger().error('Failed to calculate routes.')

    def calculate_routes(self, fleet_size):
        # Your fleet management logic goes here.
        # You should return a list of routes based on the fleet_size.
        # Replace this with your actual logic.

        if fleet_size <= 0:
            return None

        routes = ['Route_%d' % i for i in range(1, fleet_size + 1)]
        return routes

def main(args=None):
    rclpy.init(args=args)
    fleet_management_server = FleetManagementServer()
    try:
        rclpy.spin(fleet_management_server)
    except KeyboardInterrupt:
        pass
    fleet_management_server.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

