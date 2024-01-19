# -*- coding: utf-8 -*-
from naoqi import ALProxy
robot_ip = "192.168.0.108"
robot_port = 9559
tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
tts.setLanguage("Spanish")
sonarProxy = ALProxy("ALSonar", robot_ip, robot_port)       #Sensor de proximidad
sonarProxy.subscribe("myApplication")
memoryProxy = ALProxy("ALMemory", robot_ip, robot_port)     #Memoria
leds = ALProxy("ALLeds", robot_ip, robot_port)               #Leds
audio = ALProxy("ALAudioPlayer", robot_ip, robot_port)      #Audio

bandera_leds = False
print("Introduce uno de los siguientes comandos: \nhola para saludar. \nmedir para medir las distancias. \nandar, girar o lado para movimientos. \ncolor para cambiar los colores de mi pecho. \nsalir para desconectarse.\n")
while True:
    valor = raw_input("Introduce uno de los comandos: ")

    if valor == 'salir':
        #tts.say("Me voy ya")
        break
    elif valor == 'hola':
        tts.say("Hola picha")

    elif valor == 'medir':
        a = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")   #Sensor derecho
        print("%.2f" %a)
        tts.say("Hay un obstaculo a %.2f metros" %a)

    elif valor == 'andar':      #Anda hacia delante
        tts.say("Hola picha")

    elif valor == 'girar':      #Gira
        tts.say("Hola picha")

    elif valor == 'lado':       #Anda de lado
        tts.say("Hola picha")

    elif valor == 'color':       #Anda de lado
       # tts.say("Dame un color en ingles")
        color_name = raw_input("Introduce un color entre white, red, green, blue, yellow, magenta, cyan: ")
        led_name = "ChestLeds"
        if color_name == "white":
            tts.say("El color seleccionado es blanco")
            bandera_leds = True
            
        elif color_name == "red":
            tts.say("El color seleccionado es rojo")
            color_2 = "Red"
            bandera_leds = True
            
        elif color_name == "green":
            tts.say("El color seleccionado es verde")
            color_2 = "Green"
            bandera_leds = True
            
        elif color_name == "blue":
            tts.say("El color seleccionado es azul")
            color_2 = "Blue"
            bandera_leds = True
            
        elif color_name == "yellow":
            tts.say("El color seleccionado es amarillo")
            bandera_leds = True
            
        elif color_name == "magenta":
            tts.say("El color seleccionado es magenta")
            bandera_leds = True
            
        elif color_name == "cyan":
            tts.say("El color seleccionado es cyan")
            bandera_leds = True
            
        else:
            tts.say("El color introducido no es valido, intentalo de nuevo")
            bandera_leds = False
        if bandera_leds == True:
            duration = 2  # Duración en segundos
            leds.fadeRGB(led_name, color_name, duration)
            leds.setIntensity("LFoot/Led/" + color_2 + "/Actuator/Value", 0.5)
            leds.setIntensity("RFoot/Led/" + color_2 + "/Actuator/Value", 0.5)
            bandera_leds = False

    elif valor == 'reproduce':       #Reproduce un archivo
        a = audio.getMasterVolume()
        print(a)
        audio.post.playFile("/usr/share/naoqi/wav/Caballo.wav")
        audio.playFile("Caballo.wav")
        print("Esta reproduciendo")
    else:
        tts.say("no te entiendo escribe otro comando gilipollas")  #Caso en el que no dice ningun comando 