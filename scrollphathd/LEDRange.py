#!/usr/bin/env python

import scrollphathd as sphd
import time

for x in range(17):
	for y in range(7):
		sphd.set_pixel(x,y,(x*0.01)+(y*0.07))

sphd.show()

while True:
	time.sleep(1)
