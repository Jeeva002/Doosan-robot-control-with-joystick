#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# def logger(msg):
#     production = False
#     if production:
#         return""
#     else:
#         return logger(msg)


class roboCore:

    def __init__(self):
    
      self.countx = 0 
      self.robomovement=[0,0,0,0,0,0]
      self.ready_pos=[0,0,90,0,90,0]
      self.robovelocity=100
      self.roboacceleration=100
      self.homeflag=False



   
    def axes_function(self, joy_x,joy_y,joy_z,joy_rx,joy_ry,joy_rz,robo_ready_pos):
       
   
        if robo_ready_pos == 1:
           
           nameSpaceObj.movej(self.ready_pos,self.robovelocity,self.roboacceleration)   

        else:
           
           self.robomovement[0]=joy_x
           self.robomovement[1]=joy_y
           self.robomovement[2]=joy_z
           self.robomovement[3]=joy_rx
           self.robomovement[4]=joy_ry
           self.robomovement[5]=joy_rz

        
           self.robx = [0]
           self.roby = [0]
           self.robz = [0]
           self.robrx = [0]
           self.robry = [0]
           self.robrz = [0]

           self.robx.append(joy_x)
           self.roby.append(joy_y)
           self.robz.append(joy_z)
           self.robrx.append(joy_rx)
           self.robry.append(joy_ry)
           self.robrz.append(joy_rz)

           self.countx += 1 
    

    
           if self.countx == 80:
           
                 xaverage=statistics.mean(self.robx)
                 yaverage=statistics.mean(self.roby)
                 zaverage=statistics.mean(self.robz)
                 rxaverage=statistics.mean(self.robrx)
                 ryaverage=statistics.mean(self.robry)
                 rzaverage=statistics.mean(self.robrz)

                 print("average is :",xaverage)
                 print("average is :",yaverage)
                 print("average is :",zaverage)
                 print("average is :",rxaverage)
                 print("average is :",ryaverage)
                 print("average is :",rzaverage)

                 self.robomovement[0]=round(xaverage,1)
                 self.robomovement[1]=round(xaverage,1)
                 self.robomovement[2]=round(xaverage,1)
                 self.robomovement[3]=round(xaverage,1)
                 self.robomovement[4]=round(xaverage,1)
                 self.robomovement[5]=round(xaverage,1)
           
                 #nameSpaceObj.movel(self.robomovement,time=0.5, ref=DR_BASE, mod=DR_FC_MOD_REL)
                 nameSpaceObj.movel(self.robomovement,vel=100,acc=100, ref=DR_BASE, mod=DR_FC_MOD_REL)
                 sol = get_current_posx()
                 print(sol)
              
                 joyJogFlag =True 
                 self.countx=0

                 if joyJogFlag :
                 
                    self.robx.clear()
                    self.roby.clear()
                    self.robz.clear()
                    self.robrx.clear()
                    self.robry.clear()
                    self.robrz.clear()
                    joyJogFlag = False 
      
roboobj = roboCore()

def callback(data):
     
    
          joy_x=round(30*data.axes[0],1)
          joy_y=round(30*data.axes[1],1)
          joy_z=round(30*data.axes[2],1)
          joy_rx=round(30*data.axes[3],1)
          joy_ry=round(30*data.axes[4],1)
          joy_rz=round(30*data.axes[5],1)
          robo_ready_pos=data.buttons[0]
     
          roboobj.axes_function(joy_x,joy_y,joy_z,joy_rx,joy_ry,joy_rz,robo_ready_pos)
      
   
     
   




   
