import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.counter_ = 0
        self.frequency = 1.0

        self.pub_ = self.create_publisher(String, "chatter", 10)
        self.get_logger().info(f"Publishing at frequency {self.frequency}")
        self.timer = self.create_timer(self.frequency, self.timerCallback)


    def timerCallback(self):
        msg = String()
        msg.data = "Hello, the counter is {self.counter_}"
        self.pub_.publish(msg)
        self.counter_ += 1


def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()