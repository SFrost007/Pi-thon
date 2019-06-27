#!/usr/bin/env python

import scrollphathd, time

scrollphathd.rotate(180)
disp_width=scrollphathd.get_shape()[0]

length=scrollphathd.write_string("Hello world")
scrollphathd.show()
time.sleep(0.5)

for x in range(length - disp_width):
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.02)

time.sleep(0.5)

