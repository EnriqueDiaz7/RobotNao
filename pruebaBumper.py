# -*- coding: utf-8 -*-

#importamos el módulo AlProxy desde la librería naoqui para poder tabrajar
from naoqi import ALProxy

#Instanciamos el módulo AlMemory para poder acceder al valor de los sensores
memoryProxy = ALProxy("ALMemory", "nao.local", 9559)

while(1):
    #Bumper pierna izquierda. Posibles valores: 00(sin fuerza) 10(una fuerza pequeña) 11 (una fuerza mayor que la anterior)
    print(str(memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Right/Sensor/Value")) + ", " 
          + str(memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value")))
    
    #Bumper pierna derecha. Posibles valores: 00(sin fuerza) 01(una fuerza pequeña) 11 (una fuerza mayor que la anterior) 
    print(str(memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value")) + ", " 
          + str(memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Left/Sensor/Value")))