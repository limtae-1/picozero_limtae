#빨간선 VCC / 갈색선 GND / 오렌지 Pin번호
#1도를 움직이기 위해선 value 값을 0.01로 지정
#계산식은 value값이 1일때가 최대값인데 이를 계산하면 90도가 나옴
#1도를 0.01로 계산하기엔 오차가 살짝있지만 무시해보고 진행하
#서보모터 제조사에 따라 최대각도가 다른 이슈가 있음
#tiankongrc제조사는 최대각도가 90도 데이터시트 참고할것
from picozero import Servo
from time import sleep

servo = Servo(1)
'''
#이해 완료 수정하지 말 것
servo.min() #최소값인 0도로
sleep(1)
servo.mid()
#sleep(1)
#servo.max() #90도 회전
#sleep(1)
#servo.pulse()
#sleep(1)
#servo.off()
'''

'''
servo.value = 0
sleep(1)
servo.value = 1
sleep(1)
servo.value = 0.15
sleep(1)
'''

'''
for i in range(0, 200):
    servo.value = i / 100
    sleep(0.1)
'''

for i in range(0,11,1):
    servo.value = i / 10
    sleep(0.5)
    print(servo.value)
    #if servo.value==0.5996338:
     #   servo.off()
      #  break
# servo.off()
