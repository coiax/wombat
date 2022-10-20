import time
import machine
from machine import Pin
led=Pin(25,Pin.OUT)        #create LED object from pin13,Set Pin13 to output

while True:
  led.value(1)            #Set led turn on
  time.sleep(0.5)
  led.value(0)            #Set led turn off
  time.sleep(0.5)