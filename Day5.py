
import RPi.GPIO as gpio  # libreria para utilizar los puertos 
from time import sleep # es para dar pausas 

              # definimos los pines de GPIO a utiliyar 

# gpio.setmode(gpio.BCM)   # modo BCM de la raspberry pi 
# gpio.setup(led_r,gpio.OUT) # configuramos los puertos conectados a la salida 
# gpio.setup(led_y,gpio.OUT)
# gpio.setup(led_g,gpio.OUT)                           # bucle infinito 
# while True:
#     gpio.output(led1,True)   # encendemos el led1
#     sleep(1)                  # pausa de un segundo 
#     gpio.output(led1, False)  # apagamos el led1
#     sleep(1)                  # pausa de un segundo 

# ejercicio
# hacer que los tres leds parpadeen todos juntos con un intervalo dde 0.5 segundos 
led_r = 23
led_y = 24
led_g = 25

gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

tiempo = 0.5
while True:
	gpio.output(led_r,True) #encender el led1 
	sleep(0.5)              # pausa de 0.5 segundo 
	gpio.output(led_y,True) # encendemos el led2
	sleep(0.5)              # pausa de 0.5 segundos 
	gpio.output(led_g,True) # encendemos el led3
	sleep(0.5)
	gpio.output(led_g,False) # apagamos el led1 
	sleep(0.5)               # pausa de un segundo 
	gpio.output(led_y,False) # apagamos el led2
	sleep(0.5)               # pausa de un segundo 
	gpio.output(led_r,False) # apagamos el led3
	sleep(0.5)	             # pausa de un segundo 

# Ejercicio: hacer el mismo efecto con ciclo for 

lista_led = [led_r, led_y, led_g]
try:
    while True:
        for x in lista_led:
            gpio.output(x, True)
            sleep(0.5)
            gpio.output(x, False)
            sleep(0.5)
except KeyboardInterrupt:
    for y in lista_led:
        gpio.output(x, False)
       
time = 0.5 

while True:
    for d in lista_led:    # hace que se quede en el mismo 
         gpio.output(d, True)
         sleep(time)
    for f in lista_led:
         gpio.output( f, False)
         sleep(time)

