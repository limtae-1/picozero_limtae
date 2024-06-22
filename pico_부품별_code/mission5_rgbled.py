from picozero import RGBLED
from time import sleep

rgb = RGBLED(red=5, green=4, blue=3)

rgb.color = (0, 255, 255) #red #파라미터 RGB
sleep(1)
rgb.color = (0, 161, 255) #green
sleep(1)
rgb.color = (0, 27, 255) #blue 
sleep(1)
rgb.color = (255, 0, 255) #blue 
sleep(1)
rgb.color = (255, 255, 0) #blue 
sleep(1)
rgb.color = (252, 255, 153) #blue 
sleep(1)
rgb.color = (160, 255, 0) #blue 
sleep(1)
rgb.on() # white
rgb.off() # white