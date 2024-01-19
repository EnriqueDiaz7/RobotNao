
#importamos el módulo AlProxy desde la librería naoqui para poder trabajar
from naoqi import ALProxy

#Instanciamos el módulo AlMotion
motion = ALProxy("ALMotion", "nao.local", 9559)

#Inicializamos 
motion.moveInit()

#Movimiento (Recto, Izquierda, Giro (+, -))
motion.moveTo(0, 0, 0)