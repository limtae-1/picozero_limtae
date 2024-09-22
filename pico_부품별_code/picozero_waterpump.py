from picozero import WaterPump
from time import sleep

water_pump = WaterPump(pin1=15, pin2=16)

# 워터펌프를 5초 동안 정방향으로 동작
water_pump.run_for(5, direction=True)


#집에 있는 코드 추가해서 정리하기 24.09.23