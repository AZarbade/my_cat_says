# My cat says

A simple publisher and subscriber example for ROS2.

## Usage

- Clone the repo into ROS workspace, at: ros_ws/src/"here..."
- ```$ colcon build --packages-select my_cat_says```
- In termial #1,
    - ```ros2 run my_cat_says talker```
- In terminal #2,
    - ```ros2 run my_cat_says listener```
- Watch