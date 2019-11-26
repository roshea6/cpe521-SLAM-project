#!/usr/bin/env python2

"""
Description: Takes in the takes in the LaserScan message from the rear_laser
and republishes over the the front laser topic so gmapping can use it to 
build the map

Author: Ryan O'Shea

"""


import rospy 
import tf 
from sensor_msgs.msg import LaserScan
import geometry_msgs.msg
import tf.msg

def rear_laser_callback(laser_msg):
    pub = rospy.Publisher('/fused_laser', LaserScan, queue_size=1)

    scan = LaserScan()

    scan.header.stamp = laser_msg.header.stamp
    scan.header.frame_id = "rear_laser"

    scan.angle_min = -1.57
    scan.angle_max = 1.57
    scan.angle_increment = 3.14 / 180
    scan.time_increment = (1.0 / 75.0)/181
    scan.range_min = 0.0
    scan.range_max = 30.0
    scan.ranges = laser_msg.ranges
    scan.intensities = laser_msg.intensities

    pub.publish(scan)

def front_laser_callback(laser_msg):
    pub = rospy.Publisher('/fused_laser', LaserScan, queue_size=1)

    scan = LaserScan()

    scan.header.stamp = laser_msg.header.stamp
    scan.header.frame_id = "front_laser"

    scan.angle_min = -1.57
    scan.angle_max = 1.57
    scan.angle_increment = 3.14 / 180
    scan.time_increment = (1.0 / 75.0)/181
    scan.range_min = 0.0
    scan.range_max = 30.0
    scan.ranges = laser_msg.ranges
    scan.intensities = laser_msg.intensities

    pub.publish(scan)

if __name__ == '__main__':
    # Initiliaze the node
    rospy.init_node('laser_fusion', anonymous=True)

    rospy.Subscriber("front_laser", LaserScan, front_laser_callback)

    rospy.Subscriber("rear_laser", LaserScan, rear_laser_callback)

    rospy.spin()