import rclpy
from rclpy.node import Node
import screen_app.msg

# https://automaticaddison.com/how-to-write-a-ros2-publisher-and-subscriber-python-foxy/

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            screen_app.msg.Mouse, 
            '~/mouse_press', 
            self.listener_callback,
            self.store_data,
            10)

        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Mouse is at position: x: "%d", y: "%d"' % screen_app.msg.Mouse.x, screen_app.msg.Mouse.y)

    def store_data(self):
        self.x = screen_app.msg.Mouse.x
        self.y = screen_app.msg.Mouse.y

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()