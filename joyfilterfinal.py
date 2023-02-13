#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import sys
import os
import statistics
from sensor_msgs.msg import Joy


sys.dont_write_bytecode = True
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../common/imp")) ) 

ROBOT_ID     = "dsr01"        
ROBOT_MODEL  = "a0509"  

import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *

nameSpaceObj = CDsrRobot(ROBOT_ID, ROBOT_MODEL)





movement_flag = True
robomovement=[0,0,0,0,0,0]
ready_posj=[0,0,90,0,90,0]


class roboCore:

    def __init__(self):
    
      self.countx = 0 
 
      self.ready_pos=[0,0,90,0,90,0]
      self.robovelocity=100
      self.roboacceleration=100
      self.homeflag=False


   
    def axes_function(self, joy_x,joy_y,joy_z,joy_rx,joy_ry,joy_rz):
           
      
           self.rob_x = [0]
           self.rob_y = [0]
           self.rob_z = [0]
           self.rob_rx = [0]
           self.rob_ry = [0]
           self.rob_rz = [0]

           self.rob_x.append(joy_x)
           self.rob_y.append(joy_y)
           self.rob_z.append(joy_z)
           self.rob_rx.append(joy_rx)
           self.rob_ry.append(joy_ry)
           self.rob_rz.append(joy_rz)

           self.countx += 1 
     
           if self.countx == 80:
           
                 xaverage=statistics.mean(self.rob_x)
                 yaverage=statistics.mean(self.rob_y)
                 zaverage=statistics.mean(self.rob_z)
                 rxaverage=statistics.mean(self.rob_rx)
                 ryaverage=statistics.mean(self.rob_ry)
                 rzaverage=statistics.mean(self.rob_rz)

               #   print("average is :",xaverage)
               #   print("average is :",yaverage)
               #   print("average is :",zaverage)
               #   print("average is :",rxaverage)
               #   print("average is :",ryaverage)
               #   print("average is :",rzaverage)

                 robomovement[0]=round(xaverage,1)
                 robomovement[1]=round(yaverage,1)
                 robomovement[2]=round(zaverage,1)
                 robomovement[3]=round(rxaverage,1)
                 robomovement[4]=round(ryaverage,1)
                 robomovement[5]=round(rzaverage,1)

                 nameSpaceObj.amovel(robomovement, time=0.5,ref=DR_BASE, mod=DR_FC_MOD_REL)
              
              
                 joyJogFlag =True 
                 self.countx=0

                 if joyJogFlag :
                 
                    self.rob_x.clear()
                    self.rob_y.clear()
                    self.rob_z.clear()
                    self.rob_rx.clear()
                    self.rob_ry.clear()
                    self.rob_rz.clear()
                    joyJogFlag = False 

   



roboobj = roboCore()

def callback(data):
     
    
          joy_x=round(100*data.axes[0],1)
          joy_y=round(100*data.axes[1],1)
          joy_z=round(100*data.axes[2],1)
          joy_rx=round(100*data.axes[3],1)
          joy_ry=round(100*data.axes[4],1)
          joy_rz=round(100*data.axes[5],1)
          robo_ready_pos=data.buttons[0]

          roboobj.axes_function(joy_x,joy_y,joy_z,joy_rx,joy_ry,joy_rz,robo_ready_pos)

          if robo_ready_pos == 1:
           
            movej(ready_posj,vel=100,acc=100)   

         
      
   
def start():
        rospy.Subscriber("joy", Joy,callback)
        rospy.init_node('joyfilter')   
         
   
