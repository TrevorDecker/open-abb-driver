#!/usr/bin/python
import abb

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
        for jointNum = xrange(0:length(self.jointLimit_lower)):
            if newJoints[jointNum] < self.jointLimit_lower[jointNum] || \
               newJoints[jointNum] > self.jointLimit_upper[jointNum]:
                print '{0} is not within bounds {1} and {2}'.format(jointNum, \ 
                         jointLimit_lower[jointNum],jointLimit_upper[jointNum])


        #TODO add spacial constraints
         
        #passed all joint limit test 
        self.Robot.set_joints(joints)

    def fowardKinamatics(self):
        #TODO
        pass
        
    def inverseKinamatics(self):
        #TODO
        pass
