# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    display.set_pixel(0, 0, 9)
    display.set_pixel(0, 1, 9)
    display.set_pixel(1, 0, 9)
    display.set_pixel(1, 1, 9)
    sleep(500)

    display.clear()
    sleep(500)
