from picozero import Button, LED
from time import sleep #sleep(초단위)

button = Button(17)
led10 = LED(10)

while True:
    if button.is_pressed:
        led10.on()
        #led11.on()
    else:
        led10.off()
        #led11.off()
    sleep(0.1)  # 잠시 대기