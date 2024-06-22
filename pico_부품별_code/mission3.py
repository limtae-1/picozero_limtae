from picozero import DistanceSensor, LED
from time import sleep

ds = DistanceSensor(echo=20, trigger=21) #거리측정 코드
led10 = LED(10)

while True:
    dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
    print(dscm)
    if dscm > 15:
        led10.on()
    else :
        led10.off()
    sleep(0.5)
