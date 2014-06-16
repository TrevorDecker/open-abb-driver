#!/usr/bin/python

#Writen by Trevor Decker tdecker@andrew.cmu.edu version 0.0
#a script to move the abb arm to varius location displaying several fiducals
#and useing web cam to record how the fiducal looks for latter analysis 

#parts of the image that we are changing: 
# tagID
# tag faimly
# tag size
# tag position


TESTMODE = True

if not TESTMODE: 
    import abb
import time
import math
from Camera import Camera
import sys
import Tkinter
from PIL import Image,ImageTk

class State:
    stateNum = -1
    joints = []

    def __init__(self):
        pass

    #TODO add stuff for image 
    #TODO add code for auto dir creation 

#helper function when given a state number does a constant time lookup of 
#what the monitor should show and where the arm shuld be 
def lookUpState(stateNum):
    #visits = 10 #number of times to revisit a position 
    #imagesPerPosition = 100
    thisState = State()
    thisState.stateNum = stateNum
    
    #currently repeats the same operations for each visit 
    visitNum     = stateNum % visits
    stateNum     = stateNum/visits
    joint_counts = [0,0,0,0,0,0] 
    joints       = [0,0,0,0,0,0]
    for i in xrange(0,len(jointLimit_upper)):
        joint_counts[i] = (jointLimit_upper[i] - jointLimit_lower[i])/jointSteps[i]
    print jointLimit_upper
    print jointLimit_lower
    print jointSteps
    print joint_counts
    for i in xrange(0,len(jointLimit_upper)):
        joints[i] = (stateNum % joint_counts[i])*jointSteps[i] + jointLimit_lower[i]
        stateNum = stateNum/joint_counts[i]
    #TODO image selection 
    thisState.joints = joints 
    return thisState
    #end lookUp

def StartDataCollection():
    stateNum = 0 #TODO change
    while(stateNum < numStates):
        stateNum = stateNum+1
        print "Staring Data Collection: "
        if not TESTMODE:
            r = abb.Robot()

        #todo display tkenter screen 
        #todo pause until the user cliks a button 

        if(stateNum == 0):
            #tests the angle extreams first 
            for i in xrange(0,int(math.pow(2,len(jointLimit_lower)))):
                joints = jointLimit_upper[:] #copy value not refrence 
                print 'i:{0}'.format(i)
                for jointNum in xrange(0,len(jointLimit_lower)):
                    if (i >> jointNum)%2 == 0:
                        joints[jointNum] = jointLimit_lower[jointNum]
                if not TESTMODE:
                    r.set_joints(joints)

        #start to actually collect data  
        thisState = lookUpState(stateNum)
        print stateNum
        print 'Collecting data for state: {0}\n'.format(thisState.stateNum)
        print 'seting joints to: {0}\n'.format(thisState.joints)
        if not TESTMODE:
            r.set_joints(thisState.joints)
        #will not reach this point until the arm is done posistioning 
        #consider useing a diffrent name for the state
        cam.captureImage('dataCollection/'+str(thisState.stateNum)+'.bmp')
  
        #for accelerated testing
        if not TESTMODE:
            time.sleep(.2)
    #END while loop 
    cam.stopCam()
    #TODO Test code 
    #TODO setup image to Show  
    #TODO cleanup code 
    #TODO move helper code to  another file 

##################################################################
######################### END startDataCollection ################
##################################################################

#ensures that input command was well formed 
if len(sys.argv) != 2:
    raise NameError('Step to start on is need')

startStep = int(sys.argv[1])

#saved useful positions 
home = [[940.0,0.0,1455.0],[0.707,0.0,0.707,0.0]]
#position best for typing from the chair inisded the cage
use_computer_joints = [80.0,10.0,40.0,199.59,30.0,-199.2]
jointLimit_lower = [0,-30,-30,-70,-70,-70]
jointLimit_upper = [100,30,30,70,70,70]
jointSteps = [1.0,1.0,1.0,1.0,1.0,1.0] # amount to move each joint between positions 
visits = 10 #number of times to revisit a position 
imagesPerPosition = 100


assert(len(jointLimit_upper) == len(jointLimit_lower))
numPositions = 0
for i in xrange(0,len(jointLimit_upper)):
    numPositions += (jointLimit_upper[i]-jointLimit_lower[i])/jointSteps[i]

#calulate the total number states that will need to be visited 
numStates = numPositions*imagesPerPosition*visits;

print startStep
if (startStep < 0 or startStep > numStates):
    raise NameError('Start step must be between 0 and {0}'.format(numStates))
stateNum = startStep

#Set up GUI 
top = Tkinter.Tk()
#get the size of the screen inorder to make window full screen 
SCREENWIDTH, SCREENHEIGHT = top.winfo_screenwidth(),top.winfo_screenheight()
#top.overrideredirect(1)
top.geometry("%dx%d+0+0" %(SCREENWIDTH,SCREENHEIGHT))
top.focus_set() # <-- move focus to the widget
#causes pressing the esc button to close the program 
top.bind("<Escape>",lambda e:  e.widget.quit())
start_btn = Tkinter.Button(top,text="Start Data Collection",\
command = StartDataCollection,width=SCREENWIDTH,height=SCREENHEIGHT)

#Hack Camrea would not start correctly unless outside of function 
cam = Camera(0)
cam.startCam()


#start_btn.pack()
photo = Tkinter.PhotoImage(file = 'test.jpg')
top.create_image(0,0, image=photo)

top.mainloop()


