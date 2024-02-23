import rclpy
from std_msgs.msg import String

def main():
    rclpy.init(args=None)
    node = rclpy.create_node('cat')
    publisher = node.create_publisher(
        msg_type = String,
        topic = 'sound',
        qos_profile = 10)
    msg = String()
    i = 0

    def timer_callback():
        nonlocal i
        msg.data = f"meow: {i}"
        i += 1
        node.get_logger().info(f"Publishing: {msg.data}")
        publisher.publish(msg)

    period = 0.1
    timer = node.create_timer(period, timer_callback)
    rclpy.spin(node)
    node.destory_timer(timer)
    node.destory_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
