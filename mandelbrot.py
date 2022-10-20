import machine
import ssd1306
import time

def setup_display():
    # Using I2C interface Nbr 1, GPIO pins 18 and 19 for sda, scl respectively
    i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19), freq = 400000)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text("Hello world!", 0, 0, 1)
    display.show()

    return display


def membership_check(C: complex, iterations: int = 20) -> bool:
    z = 0
    for iteration in range(iterations):
        z = z**2 + C
        if abs(z) > 2:
            return False

    return True

def convert_coordinate(x: int, y: int, max_x: int, max_y: int) -> complex:
    min_i = -2.50
    max_i = +1.50
    min_j = -2j
    max_j = +2j

    delta_i = max_i - min_i
    delta_j = max_j - min_j

    x_ratio = x / max_x
    y_ratio = y / max_y

    i = min_i + (delta_i * x_ratio)
    j = min_j + (delta_j * y_ratio)

    return (i + j)


def main():
    display = setup_display()
    # Wipe display.
    display.fill(0)
    display.show()

    max_x = 128
    max_y = 64

    for x_coordinate in range(0, max_x):
        for y_coordinate in range(0, max_y):
            C = convert_coordinate(x_coordinate, y_coordinate, max_x, max_y)
            member = membership_check(C)
            #print(x_coordinate, y_coordinate, member)
            display.pixel(x_coordinate, y_coordinate, member)

    display.show()
    while True:
        time.sleep(0.1)
