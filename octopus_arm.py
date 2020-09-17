#Import Necessary Modules
import pybullet as p
import time
import pybullet_data as pda
import os

#Next Step is to connect to the cloud
physicsClient = p.connect(p.GUI)

#This sets the plane (floor). 
#planeId = p.loadURDF(os.path.join(pda.getDataPath(),"plane100.urdf"))
#planeId = p.loadURDF("plane100.urdf")
#planeId = p.loadURDF(os.path.join(pda.getDataPath(),"octopus.urdf"))
#there are 2 options, either get the urdf from my directory or transfer those files to the pda directory
#p.setAdditionalSearchPath("/home/gonzalez/github/octopus") #indexes where the computer should/can look for a file
#planeId = p.loadURDF("octopus.urdf") #option 1 get the urdf from my directory

planeId = p.loadURDF(os.path.join(pda.getDataPath(),"edgarURDF/plane100.urdf")) #option 2 transfer those urdf files to the pda directory


#Sets the gravity downward, (x,y,z)
p.setGravity(0,0,-10)

#The while loop allows the GUI to be perpetually running as <while True:> will always be true. <p.disconnect> allows the the computer to disconnect from the cloud so as to mess up future connections.  
while True:
    p.stepSimulation()
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
