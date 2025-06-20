#충격감지센서에서 계속해서 충격 감지가 나오는 이유는 충격감지센서 안에 구슬? 이 한쪽으로만 쏠려있을 경우임
#구슬이 왔다갔다해야 감지가 제대로 되니 기울여져있진 않은 지 확인할 것 !
from picozero import ShockSensor
from time import sleep

shock = ShockSensor(14)  # 충격 센서 핀

while True:
    if shock.is_shocked():
        print("⚡ 충격 감지!")
        sleep(0.3)
    else:
        print("충격없음")
        sleep(0.3)
    