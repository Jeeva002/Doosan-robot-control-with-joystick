#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import alterjoy
import rospy
import joyfilterfinal
from sensor_msgs.msg import Joy
import plan_and_execute


def main():
  joyfilterfinal.start()



if __name__ == "__main__": 
   main()
   
   while not rospy.is_shutdown():
    pass