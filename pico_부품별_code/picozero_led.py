#picozero LED
from picozero import LED
from time import sleep #sleep(초단위)
'''
LED 함수 정리 부분
1. on()
2. off()
3. blink() LED를 깜빡일 수 있게 함
'''
#=======================================
'''
#pico의 내장 LED 켜기
pico_led.on()
sleep(0.5)
pico_led.off()
sleep(0.5)
'''
#=======================================

#LED()함수 안에 파라미터 값은 Pin번호를 의미함
led10 = LED(10)
#led11 = LED(11)
#led12 = LED(12)

while True:
    led10.on()
    sleep(1)
    led10.off()
    sleep(1)
#led11.on()
#led12.on()
#sleep(2)
#led10.off() #LED 끌 수 있는 명령
#sleep(1)
#led10.blink() #LED를 한번 깜빡일 수 있는 명령어
'''
#=======================================
#신호등 만들기
led10 = LED(10)
led11 = LED(11)
led12 = LED(12)

while True:
    led10.on()
    sleep(3)
    led10.off()

    led11.on()
    sleep(3)
    led11.off()

    led12.on()
    sleep(3)
    led12.off()
'''