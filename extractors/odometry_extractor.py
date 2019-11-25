#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This message is used to extract all the messages in the odometry file and return them as an array
@author: mfahad
"""

import pandas as pd
import rospy
import tf
from nav_msgs.msg import Odometry
import geometry_msgs.msg
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
import tf.msg

def read_odometry():
    
    data_no_headers = pd.read_csv("Bicocca_2009-02-25b-ODOMETRY_XYT.csv", skiprows=0, nrows=2) 
    cnt = 0
    
    d_frame = data_no_headers.values
    
    t_odom_msgs=[]
    odom_msgs = []
    for i in range(0,83576):
        print cnt
        d_frame = data_no_headers.values
    
        t1 = rospy.Time.from_sec(float(d_frame[0,0]))
        x = float(d_frame[0,4])
        y = float(d_frame[0,5])
        th = float(d_frame[0,6])
        odom = Odometry()
        odom.header.stamp = t1
        odom.header.frame_id = "odom"
        
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
        
        # set the position
        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))
    
        # set the velocity
        odom.child_frame_id = "base_link"
        vx = (float(d_frame[1,4])-float(d_frame[0,4]))/(float(d_frame[1,0])-float(d_frame[0,0]))
        vy = (float(d_frame[1,5])-float(d_frame[0,5]))/(float(d_frame[1,0])-float(d_frame[0,0]))
        vth = (float(d_frame[1,6])-float(d_frame[0,6]))/(float(d_frame[1,0])-float(d_frame[0,0]))
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
        odom_msgs.append(odom)
        
        tf_msg = tf.msg.tfMessage()
        geo_msg = geometry_msgs.msg.TransformStamped()
        geo_msg.header.stamp = t1 
        geo_msg.header.seq = cnt
        geo_msg.header.frame_id = "odom"
        geo_msg.child_frame_id = "base_link"
        geo_msg.transform.translation.x = x
        geo_msg.transform.translation.y = y
        geo_msg.transform.translation.z = 0
        
        geo_msg.transform.rotation.x = odom_quat[0]
        geo_msg.transform.rotation.y = odom_quat[1]
        geo_msg.transform.rotation.z = odom_quat[2]
        geo_msg.transform.rotation.w = odom_quat[3]
        tf_msg.transforms.append(geo_msg)
        t_odom_msgs.append(tf_msg)
        cnt=cnt+1 
        data_no_headers = pd.read_csv("Bicocca_2009-02-25b-ODOMETRY_XYT.csv", skiprows=cnt, nrows=2)
        
    return t_odom_msgs, odom_msgs