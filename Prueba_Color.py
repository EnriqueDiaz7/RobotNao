from naoqi import ALProxy
import vision_definitions
from PIL import Image


IP = "192.168.0.107"

camProxy  = ALProxy('ALVideoDevice', IP, 9559)      #Declaro la camara

resolution = vision_definitions.kQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 30


nameId = camProxy.subscribeCamera("python_GVM", 0, 1, 13, 10)
print(nameId)

Resultado = camProxy.getImageRemote(nameId)

if Resultado == None:
    print("No se pudo capturar")
elif Resultado[6] == None: # En Resultado[6] se guarda la imagen en formato binario.
    print('No se obtuvieron datos de imagen.')
else:
    print("Holi")