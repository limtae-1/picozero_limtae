from picozero import Button, LED
from time import sleep #sleep(초단위)

button = Button(17)


#========경계선 표시========#
'''
#버튼 눌렀을 때 LED 켜기
led = LED(12)
button.when_pressed = led.on
button.when_released = led.off
'''

'''
if button.is_pressed:
    print("Button is pressed")
else:
    print("Button is released")   
    sleep(0.1)  # 잠시 대기
'''

#========경계선 표시========#
   

while True:
    if button.is_pressed:
        print("버튼이 눌렸습니다.")
    else:
        print("버튼이 안눌렸습니다.")   
    sleep(0.1)  # 잠시 대기

