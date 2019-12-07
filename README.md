# cpe521-SLAM-project
Final project for my Autonomous mobile robots course (CPE-521 F19). Implementing various SLAM algorithms in ROS and testing their effectiveness on premade dataset.

## How to use 
1. Clone this repository into your catkin_ws/src
2. Go into the extractors folder and unzip combined_updated.zip
3. Install gmapping if you don't already have it using sudo apt-get install ros-melodic-openslam-gmapping
4. Install the map_server package if you don't have it using sudo apt-get install ros-melodic-map-server
5.  Download the updated open_karto and slam_karto packages from my google drive here https://drive.google.com/open?id=1ep7-CWCoPfD3srgOuDbxI4GUeMOsprJR
6. Place the two ROS packages into your catkin_ws/src
7. Install Eigen3 using sudo apt-get install libeigen3-dev
8. Install sparse_bundle_adjustment using sudo apt-get install ros-melodic-sparse-bundle-adjustment
9. cd into your catkin_ws and call catkin_make
10. Launch the simulator using roslaunch cpe_slam slam_demo.launch 
    Set the gmapping arguement to true to use gmapping
    roslaunch cpe_slam slam_demo.launch gmapping:=true

    
    Set the karto arguement to true to use karto
    roslaunch cpe_slam slam_demo.launch karto:=true

11. cd into the extractors folder in cpe_slam and use the following command to start the bag file:
    rosbag play --clock combined_updated