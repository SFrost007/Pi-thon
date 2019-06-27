#!/usr/bin/env python

import time

import scrollphathd
from scrollphathd.fonts import font5x7

BRIGHTNESS = 0.1
DISPLAYWIDTH = 17
DELAY = 0.02
scrollphathd.rotate(180)

def hour_string():
    hours = time.localtime().tm_hour % 12
    return ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"][hours]

def min_string():
    tm_min = time.localtime().tm_min
    tens = tm_min / 10
    digits = tm_min % 10
    if tens == 0 and digits == 0:
        return "o'clock"
    elif tens == 0:
        return " ".join(["oh", digitstr(digits)])
    elif tens == 1:
        return teenstr(digits)
    elif digits == 0:
        return tenstr(tens)
    else:
        return "-".join([tenstr(tens), digitstr(digits)])

def digitstr(digit):
    return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][digit]

def teenstr(tens):
    return ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][tens]

def tenstr(tens):
    return ["", "", "twenty", "thirty", "forty", "fifty"][tens]

while True:
    scrollphathd.clear()
    timestr = " ".join([hour_string(), min_string()])
    buflen = scrollphathd.write_string(timestr, DISPLAYWIDTH+1, 0, font=font5x7, brightness=BRIGHTNESS)

    for x in range(buflen + DISPLAYWIDTH):
        scrollphathd.scroll(1, 0)
        time.sleep(DELAY)
        scrollphathd.show()

