
from time import sleep
import Adafruit_DHT as dht  # renombramos la libreria con dht 
import RPi.GPIO as GPIO  # libreria para utilizar los puertos de entrada y salida 

 # modo BCM de la raspberry pi 
led_r=23
led_y=24 
led_g=25
entrada=22
gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)
gpio.setup(entrada, gpio.IN)
def DHT11_data():
    #leemos los datos del sensor, la humedad y la temperatura 
    humi, temp = dht.read_retry(dht.DHT, 18) # pin data conectado al GPIO18
    return humi, temp 

# while True: # Bucle infinito 
#     try: # intentar esto, excepto cuando se aprete control+C
#         humedad, temperatura = DHT11_data() # llamamos a una funcion que nos retorna los
#         if humedad is not None and temperatura is not None: # comprobamos si hay datos , 
#             print("Humedad:", humedad, "temperatura:", temperatura)
#         else:
#             print("Error en la lectura del sensor")
#         # esperamos un tiempo para volver a leer el sensor, lo recomendable es 2 segundos 
#         sleep(20)
#     except KeyboardInterrupt: # Se ha pulsado CTRL+C
#         gpio.cleanup()    # Limpiamos los pines GPIO y salimos 
#         print("Programa terminado")
#         break       # con esto finalizamos por completo el programa, rompe el bucle 
# Ejercicio: hacer un programa que si la humedad sea mayor a 50 que encienda la luz 
# roja, si es menor a 50 que encienda la luy verde 
# humedad > 50 ------> encender solo luz roja 
# humedad < 50 ------> encender solo la luz verde
# si terminan esto pueden explayarse y hacer algo mas jaja


while True:  
    try: 
        humedad, temperatura = DHT11_data() 
        print("Humedad:", humedad, "temperatura:", temperatura)
        if humedad > 50: 
            gpio.output(led_r, True)
            gpio.output(led_g, False)
        else:
            gpio.output(led_r, False)
            gpio.output(led_g, True)
        
            sleep(20)
    except KeyboardInterrupt:
        gpio.cleanup()     
        print("Programa terminado")
        break       