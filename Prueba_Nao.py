# -*- coding: utf-8 -*-
from naoqi import ALProxy
robot_ip = "192.168.0.108"
robot_port = 9559
tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
tts.setLanguage("Spanish")
sonarProxy = ALProxy("ALSonar", robot_ip, robot_port)       #Sensor de proximidad
sonarProxy.subscribe("myApplication")                       
memoryProxy = ALProxy("ALMemory", robot_ip, robot_port)     #Memoria
leds = ALProxy("ALLeds", robot_ip, robot_port)              #Leds
audio = ALProxy("ALAudioPlayer", robot_ip, robot_port)      #Audio
motion = ALProxy("ALMotion", robot_ip, robot_port)             #Movimiento


motion.moveInit()       #Inicializacion de los motores
bandera_leds = False
print("Introduce uno de los siguientes comandos: \nhola para saludar. \nmedir para medir las distancias. \nrecto, atras, girar o izq o der para movimientos. \ncolor para cambiar los colores de mi pecho. \nencender para encender los ojos del robot. \napagar para apagar los leds de la cara. \npierna para activar los bumpers de las piernas. \nsalir para desconectarse. \n info para recargar los comandos\n")
while True:
    valor = raw_input("Introduce uno de los comandos: ")

    if valor == 'salir':
        tts.say("Hasta la próxima")
        break
    elif valor == 'hola':
        tts.say("Hola como estas")

    elif valor == 'medir':
        a = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")   #Sensor derecho
        print("%.2f" %a)
        tts.say("Hay un obstaculo a %.2f metros" %a)

    elif valor == 'recto':      #Anda hacia delante
        a = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        if a <= 0.5:
            tts.say("hay un obstaculo a %.2f metros, no puedo andar" %a)
        else:
            #tts.say("Un pasito palante maría")
            bool_andar = True
            for i in range(0, 2):
                if bool_andar == True:
                    a = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
                    if a >= 0.5:
                        motion.moveTo(0.4, 0, 0)              #Movimiento (Recto, Izquierda, Giro (+, -))
                        bool_andar = True
                    else:
                        tts.say("Hay un obstaculo %.2f metros, no puedo seguir andando" %a)
                        bool_andar = False

    elif valor == 'atras':      #atras
        tts.say("Ando hacia detras")
        motion.moveTo(-0.5, 0, 0)

    elif valor == 'izq':       #Anda de lado
        tts.say("ando a la izquierda")
        motion.moveTo(0, 0.5, 0)

    elif valor == 'der':       #Anda de lado
        tts.say("ando a la derecha")
        motion.moveTo(0, -0.5, 0)

    elif valor == 'girar':       #gira
        tts.say("Cuidado que voy a girar")
        motion.moveTo(0, 0, 2.5)

    elif valor == 'color':       #Anda de lado
        tts.say("Dame un color en ingles")
        color_name = raw_input("Introduce un color entre white, red, green, blue, yellow, magenta, cyan: ")
        led_name = "ChestLeds"
        if color_name == "white":
            tts.say("El color seleccionado es blanco")
            bandera_leds = True
            
        elif color_name == "red":
            tts.say("El color seleccionado es rojo")
            bandera_leds = True
            
        elif color_name == "green":
            tts.say("El color seleccionado es verde")
            bandera_leds = True
            
        elif color_name == "blue":
            tts.say("El color seleccionado es azul")
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
            bandera_leds = False

    elif valor == "encender":       #Encende los ojos de colores
        leds.randomEyes(1)

    elif valor == "apagar":       #Apaga los ojos de colores
        leds.off("FaceLeds")

    elif valor == "info":       #Recarga los comandos posibles
        print("Introduce uno de los siguientes comandos: \nhola para saludar. \nmedir para medir las distancias. \nrecto, atras, girar o izq o der para movimientos. \ncolor para cambiar los colores de mi pecho. \nencender para encender los ojos del robot. \napagar para apagar los leds de la cara. \npierna para activar los bumpers de las piernas. \nsalir para desconectarse. \n info para recargar los comandos\n")

    elif valor == "pierna":
        bool_izq = False
        bool_der = False
        if memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Right/Sensor/Value") != 0 or memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value") != 0:
            bool_izq = True
        if memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value") != 0 or memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Left/Sensor/Value") != 0:
            bool_der = True

        if bool_izq and bool_der:       #Si estan tocando ambas piernas
            tts.say("Noto algo en ambas piernas")
        elif bool_izq == False and bool_der:
            tts.say("Noto algo en mi pierna derecha")
        elif bool_der == False and bool_izq:
            tts.say("Noto algo en mi pierna izquierda")
        else:
            tts.say("No noto nada en ningunda de mis piernas")

    else:
        tts.say("no te entiendo, prueba con otro comando por favor")  #Caso en el que no dice ningun comando 