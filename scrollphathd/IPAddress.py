#!/usr/bin/env python

import socket, time
import scrollphathd

from scrollphathd.fonts import font5x7

def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    return s.getsockname()[0]

scrollphathd.rotate(180)
scrollphathd.write_string("  IP: " + getNetworkIp(), x=0, y=0, font=font5x7, brightness=0.05)

while True:
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.02)

