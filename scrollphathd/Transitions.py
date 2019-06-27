#!/usr/bin/env python

import scrollphathd as sphd
import time

class Directions:
    LEFT = 0
    RIGHT = 1

def sweep(direction=Directions.LEFT,delay=0.02):
    startx = sphd.width if direction == Directions.LEFT else 0
    endx = 0 if direction == Directions.LEFT else sphd.width
    step = -1 if direction == Directions.LEFT else 1

    for x in range(startx, endx, -1):
        sphd.clear_rect(x+(-3*step), 0, 1, sphd.height)
        sphd.fill(0.01, x+(-2*step), 0, 1, sphd.height)
        sphd.fill(0.1, x+(-1*step), 0, 1, sphd.height)
        sphd.fill(0.5, x, 0, 1, sphd.height)
        sphd.show()
        time.sleep(delay)

def set_test_text():
    sphd.rotate(180)
    sphd.clear()
    sphd.write_string("Test", brightness=0.1)
    sphd.show()
    time.sleep(1)

# Transition test
set_test_text()
sweep()
time.sleep(1)
set_test_text()
sweep(direction=Directions.RIGHT)

