#Import Necessary Modules
import pybullet as p
import time
import pybullet_data as pda
import os

#Next Step is to connect to the cloud
physicsClient = p.connect(p.GUI)

#This sets the plane (floor). 
planeId = p.loadURDF(os.path.join(pda.getDataPath(),"plane100.urdf"))

#Sets the gravity downward, (x,y,z)
p.setGravity(0,0,-10)

#The while loop allows the GUI to be perpetually running as <while True:> will always be true. <p.disconnect> allows the the computer to disconnect from the cloud so as to mess up future connections.  
while True:
    p.stepSimulation()
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
