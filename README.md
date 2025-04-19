# wenqing-zhang
Reference:&#x20;

[Ericsii/ros\_wit\_imu\_node: Provide wt901c IMU driver node for ROS2.](https://github.com/Ericsii/ros_wit_imu_node)

step 1\:the hardware connection

According to the DatasheetWT901C TTL Datasheet you uploaded:

*   VCC → 5V
*   GND → GND
*   RX → TX of USB-TTL module
*   TX → RX of the USB-TTL module.

Plug the IMU into the Ubuntu system and identify the port as /dev/ttyUSB0

how to view port：ls /dev/ttyUSB\*

step2：ROS 2 Humble Install Witmotion IMU

reference:

[ElettraSciComp/witmotion\_IMU\_ros at ros2](https://github.com/ElettraSciComp/witmotion_IMU_ros/tree/ros2)

download package：

    cd ~/ros2_ws/src
    git clone -b ros2 --recursive https://github.com/ElettraSciComp/witmotion_IMU_ros.git witmotion_ros
    colcon build --packages-select witmotion_ros
    source install/setup.bash


launch：

    ros2 run witmotion\_ros witmotion\_ros\_node --ros-args --params-file \~/ros2\_ws/src/witmotion\_ros/config/wt901.yml

WT901c yaml：

port：ttyusb0      baudrate:9600
 
