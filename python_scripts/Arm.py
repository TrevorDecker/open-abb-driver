#!/usr/bin/python
import abb
import math
import time

class Arm:
    #refrence to the robot 
    robot = ""
    jointLimit_lower = [0,0,0,0,0,0]
    jointLimit_upper = [0,0,0,0,0,0]
    
    def __init__(self):
        self.robot = abb.Robot();
        #TODO consider calibrating 
        #TODO consider forceing that safe region be set now 

    def __del__(self):
        #TODO
        pass

    def goHome(self):
        home_pose = [[940.0,0.0,1455.0],[0.707,0.0,0.707,0.0]];
        self.robot.set_cartesian(home_pose);

    def setJointLimitLower(self,newLimit,jointNum):
        self.jointLimit_lower[jointNum] = newLimit; 

    def setJointLimitUpper(self,jointLimit,jointNum):
        self.jointLimit_upper[jointNum] = newLimit; 
        
        
        #safe method for seting robots joints
    def setJoints(self,newJoints):
        print 'Attempting to sets joints to {0}'.format(newJoints)
#        for jointNum in xrange(0,len(self.jointLimit_lower)):
#            if newJoints[jointNum] < self.jointLimit_lower[jointNum] or \
#               newJoints[jointNum] > self.jointLimit_upper[jointNum]:
#                raise NameError('{0} is not within bounds {1} and {2}\n'.format(jointNum,\
#jointLimit_lower[jointNum],jointLimit_upper[jointNum]))
#
#
#        #TODO add spacial constraints
#         
#        #passed all joint limit test 
        val = self.robot.set_joints(newJoints)
        print val
        time.sleep(1)
        print 'Done'

    def fowardKinamatics(self):
        #TODO
        pass
        
    def inverseKinamatics(self):
        #TODO
        pass

    #a method which goes to each of the joint extreams and
    #  trys the arm at those locations so as to checks if any
    # collisions will occur while a person is still here 
    def checkLimits(self):
       for i in xrange(0,int(math.pow(2,len(self.jointLimit_lower)))):
           joints = self.jointLimit_upper
           for jointNum in xrange(1,len(self.jointLimit_lower)+1):
               if i % jointNum == 0:
                   joints[jointNum] = self.jointLimit_lower[jointNum]
           self.setJoints(joints)
           time.sleep(1)# delays for 1 second 
