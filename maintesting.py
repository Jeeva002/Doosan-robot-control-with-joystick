#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import joyfilter
from sensor_msgs.msg import Joy

def start():

        
        rospy.Subscriber("joy", Joy,joyfilter.callback)
        rospy.init_node('joyfilter')
 
if __name__ == "__main__": 
   while not rospy.is_shutdown():
    start()