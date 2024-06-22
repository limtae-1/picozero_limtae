#총 프로젝트 합본
from picozero import LED
from picozero import DistanceSensor
from time import sleep #sleep(초단위)

led10 = LED(10)
led11 = LED(11)
led12 = LED(12)

ds = DistanceSensor(echo=21, trigger=20) #거리측정 코드 #숫자는 핀번호
dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
print(dscm)
sleep(0.2)


while True:
    ds = DistanceSensor(echo=21, trigger=20) #거리측정 코드 #숫자는 핀번호
    dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
    print(dscm)
    sleep(0.2)
    if dscm >= 10:
        led10.on()
        sleep(0.5)
        led10.off()
    elif 5 < dscm < 10:
        led11.on()
        sleep(0.5)
        led11.off()
    else:
        led12.on()
        sleep(0.5)
        led12.off()
