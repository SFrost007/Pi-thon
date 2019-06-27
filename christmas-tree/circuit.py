from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep

tree = LEDBoard(*range(2,28),pwm=True)
for led in tree:
    led.on()
    print led
    sleep(2)
    led.off()

