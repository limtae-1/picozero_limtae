from picozero import Servo
from time import sleep

#기존의 서보모터 클래스에서 제어를 쉽게하기 위해 커스텀 한것

ser=Servo(14)
ser.min() #서보모터의 최소각도 0도
sleep(1)
ser.max() #서보모터의 최대각도 180도
sleep(1)
ser.mid() #서보모터의 중간각도 90도
sleep(1)
ser.value=120 #서보모터의 각도 값 설정 30도
sleep(1)
ser.pulse(0,180) #0도 부터 180도 까지 각도 변경
sleep(1)

