#!/usr/bin/env python

import scrollphathd as sphd
import time

xAdd = 1
x = 0
y = 0

while True:
	x += xAdd
	if (x == 0 or x == 16):
		xAdd *= -1
		y += 1
		if (y == 7):
			y = 0
	sphd.clear()
	sphd.set_pixel(x, y, 0.5)
	sphd.show()
	time.sleep(0.01)

