import sys
import time
import math
from naoqi import ALProxy

robotIP = "192.168.0.107"

motionProxy = ALProxy("ALMotion", robotIP, 9559)    #Declaro funcion motionProxy para mover

postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)     #Para poner postura inicial

pNames = "Body"
pStiffnessLists = 1.0
pTimeLists = 1.0

postureProxy.goToPosture("StandInit", 0.5)  #Llevo la cabeza al estado inicial 

motionProxy.wbEnableEffectorControl("LArm", True)       #Partes del cuepo: RArm, Larm, Head, 

motionProxy.wbSetEffectorControl("LArm", [0.5, 0.5, 1.])