from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    A = button_a.is_pressed()
    B = button_b.is_pressed()

    if A:
        display.set_pixel(2, 2, 9)

    if B:
        display.set_pixel(2, 2, 0)

    sleep(10)
