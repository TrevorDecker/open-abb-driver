#!/usr/bin/python

#Writen by Trevor Decker tdecker@andrew.cmu.edu version 0.0
#a script to move the abb arm to varius location displaying several fiducals
#and useing web cam to record how the fiducal looks for latter analysis 

import abb
import time
import math
from Camera import Camera
from Arm import Arm

#thisArm = Arm();

#saved useful positions 
home = [[940.0,0.0,1455.0],[0.707,0.0,0.707,0.0]]
#position best for typing from the chair inisded the cage
use_computer_joints = [80.0,10.0,40.0,199.59,30.0,-199.2]
#thisArm.checkLimits()
r = abb.Robot()
#r.set_joints(use_computer_joints)
jointLimit_lower = [0,30,-30,-70,-70,-70]
jointLimit_upper = [100,30,30,70,70,70]
for i in xrange(0,int(math.pow(2,len(jointLimit_lower)))):
    joints = jointLimit_upper[:] #copy value not refrence 
    print 'i:{0}'.format(i)
    for jointNum in xrange(0,len(jointLimit_lower)):
        print jointNum
        if (i >> jointNum)%2 == 0:
            joints[jointNum] = jointLimit_lower[jointNum]
    print joints
    r.set_joints(joints)
    
    time.sleep(.2)



#thisArm.setJoints([0,0,0,0,0,0,0])


#time.sleep(1)# delays for 1 second 


