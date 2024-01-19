import sys
import time
import math
from naoqi import ALProxy
import time

ip = "192.168.0.107"

tts = ALProxy("ALTextToSpeech", "192.168.0.107", 9559)

sonarProxy = ALProxy("ALSonar", ip, 9559)       #Sensor de proximidad

sonarProxy.subscribe("myApplication")

memoryProxy = ALProxy("ALMemory", ip, 9559)
while(1):
    memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")        #Sensor izquierdo
    a = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")   #Sensor derecho
    if (a < 0.5):
        tts.say("Oju pare que me voy a mata")
    time.sleep(1)
    print(a)

