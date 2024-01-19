# -*- coding: utf-8 -*-

import naoqi

nao_ip = "192.168.0.107"  # Reemplaza con la IP de tu robot
nao_port = 9559

# Crear una lista de palabras clave a reconocer
palabras_clave=["hola", "adiós"]

# Crear una función de callback para manejar los eventos de reconocimiento de voz
def on_detected(value):
    print("Palabra clave detectada:", value)

# Intentar conectarse al robot NAO y configurar el reconocimiento de voz
try:
    # Conectarse al robot NAO
    session = naoqi.Session()
    session.connect("tcp://" + nao_ip + ":" + str(nao_port))

    # Obtener el servicio de reconocimiento de voz
    speech_service = session.service("ALSpeechRecognition")

    speech_service.setVocabulary(palabras_clave, False)

    # Suscribirse al evento de reconocimiento de voz
    speech_service.subscribe("mi_reconocimiento")
    speech_service.signal.connect(on_detected)

    # Iniciar el reconocimiento de voz
    speech_service.pause(False)

    # Esperar a que el reconocimiento esté en curso
    print("Habla al robot NAO...")
    print("Presiona Enter para detener.\n")

    # Detener el reconocimiento de voz
    speech_service.pause(True)
    speech_service.unsubscribe("mi_reconocimiento")

except Exception as e:
    print("Error al conectarse al robot NAO:", e)
