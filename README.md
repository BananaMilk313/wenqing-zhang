#  collaborative work


## reference：
1. cra-ros-pkg/robot_localization: robot_localization is a package of nonlinear state estimation nodes. The package was developed by Charles River Analytics, Inc. Please ask questions on answers.ros.org.  
2. geographiclib/geographiclib: Main repository for GeographicLib

---

## Download the robot-localization package:


    cd ~/ekf_ws/src
    git clone https://github.com/cra-ros-pkg/robot_localization.git
    colcon build 
    source install/setup.bash


## Launch robot localization package:


    source install/setup.bash
    ros2 launch robot_localization dual_ekf_navsat.launch.py


We modified the dual_ekf_navsat_custom.launch file and the dual_ekf_navsat_custom.yaml files



