
#importamos el módulo AlProxy desde la librería naoqui para poder trabajar
from naoqi import ALProxy

#Instanciamos el módulo AlTextToSpeech
TextToSpeech = ALProxy("ALTextToSpeech", "nao.local", 9559)

#Seleccionamos el idioma
TextToSpeech.setLanguage("Spanish")

#Ponemos lo que queremos que diga
TextToSpeech.say("¡Hola!")