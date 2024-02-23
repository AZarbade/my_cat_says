import rclpy
from std_msgs.msg import String

def main():
    rclpy.init(args=None)
    node = rclpy.create_node('owner')
    subscription = node.create_subscription(
        msg_type = String,
        topic = 'sound',
        callback = lambda msg: node.get_logger().info(f"My cat says: {msg.data}"),
        qos_profile = 10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
