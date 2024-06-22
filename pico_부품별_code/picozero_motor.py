#실행을 시켜도 안돌아가는 경우는 손으로 살짝 돌려주면 알아서 돌아감
from picozero import Motor
from time import sleep

motor = Motor(18, 19)

while True:
    motor.on(speed=0.7) #모터 켜기
    motor.off() #모터 끄기

#motor.start() #모터 시작
#motor.stop() #모터 멈춤