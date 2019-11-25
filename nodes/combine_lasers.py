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

def laser_callback(laser_msg):
    pub = rospy.Publisher('/front_laser', LaserScan, queue_size=1)

    laser = laser_msg

    # Might want to take this out so it shows that both front and back
    # laser are being published on the topic that gmapping listens to
    laser.header.frame_id = "front_laser"

    pub.publish(laser)

if __name__ == '__main__':
    # Initiliaze the node
    rospy.init_node('laser_fusion', anonymous=True)

    rospy.Subscriber("rear_laser", LaserScan, laser_callback)

    rospy.spin()