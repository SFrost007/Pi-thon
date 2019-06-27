#!/usr/bin/env python

import sys, time
import scrollphathd as sphd
from scrollphathd.fonts import font5x7
import pyowm

owm = pyowm.OWM("4e4f54f09149cf1d050143b7238a2ed3")
obs = owm.weather_at_place("Cambridge, UK")
w = obs.get_weather()
status = w.get_detailed_status()


sphd.rotate(180)
sphd.write_string(status+"  .", x=0, y=0, font=font5x7, brightness=0.5)

while True:
    sphd.show()
    sphd.scroll()
    time.sleep(0.01)
