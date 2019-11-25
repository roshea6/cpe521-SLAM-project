#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This file reads laser data and returns it in form of an array

@author: mfahad
"""
import pandas as pd
import rospy
import tf
from sensor_msgs.msg import LaserScan
import geometry_msgs.msg
import tf.msg

def read_laser(file_name):
    data_no_headers = pd.read_csv(file_name, skiprows=0, nrows=1) 
    cnt = 0

    d_frame = data_no_headers.values
    t_odom_msg = []
    laser_msg=[]
    while len(data_no_headers.values)>=1:
        print cnt
        t1 = rospy.Time.from_sec(float(d_frame[0,0]))
        d_frame = data_no_headers.values
        
        tf_msg = tf.msg.tfMessage()
        geo_msg = geometry_msgs.msg.TransformStamped()
        geo_msg.header.stamp = t1 
        geo_msg.header.seq = cnt
        geo_msg.header.frame_id = "base_link"
        geo_msg.child_frame_id = "front_laser"
        geo_msg.transform.translation.x = 0.08
        geo_msg.transform.translation.y = 0
        geo_msg.transform.translation.z = 0.45
        angles = tf.transformations.quaternion_from_euler(0,0,0) 
        geo_msg.transform.rotation.x = angles[0]
        geo_msg.transform.rotation.y = angles[1]
        geo_msg.transform.rotation.z = angles[2]
        geo_msg.transform.rotation.w = angles[3]
        tf_msg.transforms.append(geo_msg)
        t_odom_msg.append(tf_msg)
    
        scan = LaserScan()

        scan.header.seq = cnt
        scan.header.stamp = t1
        scan.header.frame_id = "front_laser"
    
        scan.angle_min = -1.57
        scan.angle_max = 1.57
        scan.angle_increment = 3.14 / 180
        scan.time_increment = (1.0 / 75.0)/181
        scan.range_min = 0.0
        scan.range_max = 30.0
        scan.ranges = []
        scan.intensities = []
        for j in range(3, 184):
            scan.ranges.append(float(d_frame[0,j]))  
        laser_msg.append(scan) 

        
        cnt=cnt+1 
        data_no_headers = pd.read_csv(file_name, skiprows=cnt, nrows=1)
    return t_odom_msg,laser_msg