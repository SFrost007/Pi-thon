from gpiozero import LEDBoard, PWMLED
from gpiozero.tools import random_values
from signal import pause
from time import sleep

#tree = LEDBoard(*range(2,28),pwm=True)
#for led in range(2,28):
#  poo=PWMLED(led)
#  print led
#  poo.on()
#  sleep(10)
#  poo.off()

star = PWMLED(2)
star.pulse()


row1=[19]
row2=[11,27,17,25,16]
row3=[8,26,5,4,9,13]
row4=[6,18,15,12,22,24,20]
row5=[7,21,14,10,23]
rows=[row1,row2,row3,row4,row5]

lights=[]

#while True:

for item in rows:
  for lednum in item:
    light = PWMLED(lednum)
    light.blink(on_time=0.1,off_time=1,fade_in_time=0.1,fade_out_time=0.1)
    lights.append(light)
  sleep(0.1)

#  sleep(0.1)

#  for light in lights:
#    light.close()
#  lights = []
#
#  for item in reversed(rows):
#    for lednum in item:
#      light = PWMLED(lednum)
#      light.blink(on_time=0.1,off_time=1,fade_in_time=0.1,fade_out_time=0.1)
#      lights.append(light)
#    sleep(0.1)
#
#  for light in lights:
#    light.close()
#  lights = []
#
#  sleep(0.1)






  #for lednum in item:
    #light = PWMLED(lednum)
    #light.off()
    #light.close()


    #light.on()
    #light.pulse()
    #light.blink(on_time=0.5,off_time=2,fade_in_time=0.5,fade_out_time=0.5)



#tree.blink(on_time=0.5, off_time=1, fade_in_time=1)

#bf = PWMLED(8)
#bf.on()


pause()

