#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image,CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from darknet_ros_msgs.msg import BoundingBoxes,BoundingBox
import cv2
from subprocess import call, Popen

def pic_sub():#when I use it, it did loop or not save capture. in 2021/05/06
    rospy.init_node('get_picture')
    rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, call_getpic)

    # Ctrl + C fin
    r = rospy.Rate(1.0)
    r.sleep()
    
    #rospy.spin()
    #callback()
    print("finished")

def call_getpic(data):
    global senddarky, senddarkx
    #print(data.bounding_boxes[0].xmin)
    #print(data.bounding_boxes[0])
    posx = int((data.bounding_boxes[0].xmin + data.bounding_boxes[0].xmax)/2)
    posy = int((data.bounding_boxes[0].ymin + data.bounding_boxes[0].ymax)/2)
    #print (posx)
    senddarkx = str(posx)
    senddarky = str(posy)
    print(senddarkx, senddarky)
    call("rosnode kill /darknet_ros", shell=True)
    #call("rosnode kill /picture_data", shell=True)
    return 'grasp'
#==========================================

if __name__ == '__main__':
    print("Please Speak")
    pic_sub()