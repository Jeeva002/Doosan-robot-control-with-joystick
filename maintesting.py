#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import joyfilterfinal




def main():
  joyfilterfinal.start()



if __name__ == "__main__": 
   main()
   
   while not rospy.is_shutdown():
    pass
