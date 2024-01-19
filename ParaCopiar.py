# -*- coding: utf-8 -*-
from naoqi import ALProxy

# Configuración de la conexión al robot
robot_ip = "192.168.0.108"
robot_port = 9559

file_manager = ALProxy("ALFileManager", robot_ip, robot_port)
audio = ALProxy("ALAudioPlayer", robot_ip, robot_port)      #Audio

ruta_sonido_original = "/path/to/Caballo.wav"
ruta_sonido_destino = "/path/to/Caballo.wav"  # Puedes especificar una ruta diferente en el robot si lo deseas

fileId = audio.loadFile("C:\Users\jinie\Desktop\Caballo.wav")
audio.playFile(fileId)
print(fileId)