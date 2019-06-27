#!/usr/bin/env python

import sys, time
import scrollphathd

from scrollphathd.fonts import font5x7

scrollphathd.rotate(180)

scrollphathd.write_string("          " + str(sys.argv[1]), x=0, y=0, font=font5x7, brightness=0.05)

while True:
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.02)

