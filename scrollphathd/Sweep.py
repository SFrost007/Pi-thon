#!/usr/bin/env python

import scrollphathd as sphd
import time

class Directions:
    up = 0
    down = 1
    left = 2
    right = 3

def sweep():
    for x in xrange(sphd.width, 0, -1):
        sphd.clear_rect(x+3, 0, 1, sphd.height)
        sphd.fill(0.01, x+2, 0, 1, sphd.height)
        sphd.fill(0.1, x+1, 0, 1, sphd.height)
        sphd.fill(0.5, x, 0, 1, sphd.height)
        sphd.show()
        time.sleep(0.02)

# Setup a starter display
sphd.rotate(180)
sphd.write_string("Test", brightness=0.1)
sphd.show()
time.sleep(1)

# Transition test
sweep()

