from picozero import TouchSensor
from time import sleep

touch = TouchSensor(14)  # 터치 센서 핀

while True:
    if touch.is_touched():
        print("🖐터치 감지됨!")
        sleep(0.5)
    else:
        print("터치 감지 안됨!")
        sleep(0.5)