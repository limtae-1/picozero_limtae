from picozero import LightSensor
from time import sleep

#조도 센서 특성상 GP 26,27,28 중 하나여야함
#밝기의 단위는 룩스(LUX)지만 우리가 쓰는 조도센서는 정확한lux값 측정 불가
#우리가 사용하는 밝기(%)는 주변 조명 상황에 따라 달라지는 상대값
#0~100%는 **"상대적인 밝기 비율"**로, 주변 환경의 밝고 어두움을 직관적으로 표현한 것
sensor = LightSensor(27)  # ADC0: GP26

while True:
    brightness = sensor.brightness()
    print("밝기:", brightness, "%")
    sleep(0.5)