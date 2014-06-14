#!/usr/bin/python

#Writen by Trevor Decker tdecker@andrew.cmu.edu version 0.0
#a script to move the abb arm to varius location displaying several fiducals
#and useing web cam to record how the fiducal looks for latter analysis 

import abb
import time
from Camera import Camera
from Arm import Arm

thisArm = Arm();

#saved useful positions 
home = [[940.0,0.0,1455.0],[0.707,0.0,0.707,0.0]]
#position best for typing from the chair inisded the cage
use_computer_joints = [80.0,10.0,40.0,199.59,30.0,-199.2]



