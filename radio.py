import machine
import random
import ssd1306
import math

led = machine.Pin(25, machine.Pin.OUT)
radio_adc = machine.ADC(0)
radio = machine.Pin(13, machine.Pin.IN)

def setup_display():
    # Using I2C interface Nbr 1, GPIO pins 18 and 19 for sda, scl respectively
    i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19), freq = 400000)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    return display

display = setup_display()

def update_display_from_radio(timestamp):
    #ratio = radio_adc.read_u16() / 65535
    ratio = radio.value()

    min_y = 10
    may_y = 50
    delta_y = may_y - min_y

    y = math.trunc(min_y + delta_y * ratio)

    for i in range(64):

        if i == y:
            color = 1
        else:
            color = 0
        display.pixel(0, i, color)

    display.scroll(1, 0)
    display.show()

def main():
    display.fill(0)
    display.show()

    timer = machine.Timer(
        period=25,
        mode=machine.Timer.PERIODIC,
        callback=update_display_from_radio
    )
