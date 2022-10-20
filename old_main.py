import time
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C

import mandelbrot
mandelbrot.main()

 # This does U2C scan
 # BLinking LED
 # Read internal temperature
 # Display temp on I2C OLED device, updating every few seconds
 
 #Using I2C interface Nbr 1, GPIO pins 18 and 19 for sda, scl respectively
i2c = I2C(1, sda=Pin(18), scl=Pin(19), freq = 400000)

# Get the list of all I2C devices
listOfAddresses = ""
for someAddr in i2c.scan():
    listOfAddresses+= f'{someAddr:3}'
print("List of all I2C Devices:", listOfAddresses)

# Set up OLED and display data
oled = SSD1306_I2C(128, 64, i2c)
oled.text('Welcome', 0, 0)
#oled.text('This is wombat', 0, 24)
oled.text(('i2c addrs:' + listOfAddresses), 0, 48)
oled.show()

# Set up LED to flash
led=Pin(25,Pin.OUT)        #create LED object from pin13,Set Pin13 to output

# set up tempeartuar sensor
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)


while True:
    # Flashing the LED
    led.value(1)            #Set led turn on
    # Temperature sensor
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    oled.fill(0) 
    oled.text('Temp='  + f'{temperature:3}', 0, 24)
    oled.show()
    time.sleep(1)
    # Now with LED off
    led.value(0)            #Set led turn off
    oled.fill(0)
    oled.show()
    time.sleep(1)

