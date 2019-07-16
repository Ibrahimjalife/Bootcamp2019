
import RPi.GPIO as gpio
from time import sleep 

# Ejercicio: con la primera pulsacion encender solo el primer led
# con la segunda pulsacion, encender solo el segundo led 
# con la tercera pulsacion, encender solo el tercer led 

led_r=23
led_y=24 
led_g=25
entrada=22
gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)
gpio.setup(entrada, gpio.IN) # configuramos como entrada
contador=0                   # variable para manejo de los leds 
while True:                  # bucle infinito 
    if gpio.input(entrada):  # 
         contador = contador + 1 #3 #aumentamos la variable contador 
        # como solo tenemos un led, contador debe tomar los valores 0,1 
         sleep(0.3)
    if contador == 4:
         contador = 0  # pero usamos el 0 para apagar el led 
    if contador == 0:
         gpio.output(led_r, False) # apagamos todos los leds 
         gpio.output(led_y, False)
         gpio.output(led_g, False)
    if contador == 1:
         gpio.output(led_r, True) # encendemos el led1 y apagamos los restantes  
         gpio.output(led_y, False)   
         gpio.output(led_g, False)
    if contador == 2:
         gpio.output(led_r, False) 
         gpio.output(led_y, True) # encendemos el led2 y apagamos los restantantes 
         gpio.output(led_g, False)
    if contador == 3:
         gpio.output(led_r, False)
         gpio.output(led_y, False)
         gpio.output(led_g, True) # endendemos el led3 y apagamos los restantes
    
   


