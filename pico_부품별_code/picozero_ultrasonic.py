from picozero import DistanceSensor
from time import sleep

ds = DistanceSensor(echo=20, trigger=21) #거리측정 코드

'''
dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
print(dscm)
sleep(0.2)
'''
while True:
    dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
    print(dscm)
    sleep(0.5)
