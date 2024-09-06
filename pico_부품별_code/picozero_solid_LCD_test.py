'''
from picozero import SoilMoistureSensor, I2C_LCD
from time import sleep

#같이 써야하는 클래스도 정의함.
#아래 코드는 습도를 0~1로만 표현
#0은 건조에 가까운 것 1은 습함의 가까운 정도

sensor = SoilMoistureSensor(pin=26, min_value=20000, max_value=50000)
lcd = I2C_LCD(scl=21, sda=20)
lcd.clear()

while True:
    moisture_percentage = round(sensor.read_percentage(),2)
    a=str(moisture_percentage)
    b=a+"%"
    lcd.putstr(b, col=0, row=0)
    print("Soil Moisture: {:.2f}%".format(moisture_percentage))
    
    sleep(1)
'''

from picozero import SoilMoistureSensor, I2C_LCD
from time import sleep

# 토양 습도 센서 설정 (min_value, max_value 설정)
sensor = SoilMoistureSensor(pin=26, min_value=20000, max_value=50000)

# I2C LCD 설정 (SCL=21, SDA=20 핀 사용)
lcd = I2C_LCD(scl=21, sda=20)
lcd.clear()

while True:
    # 습도를 소수점 둘째 자리까지 읽어옴
    moisture_percentage = round(sensor.read_percentage(), 2)
    
    # 소수점 둘째 자리까지 문자열로 변환하고 % 기호 붙임
    b = "{:.2f}%".format(moisture_percentage)
    
    # LCD에 출력
    lcd.clear()  # 화면을 지우고 출력
    lcd.putstr(b, col=0, row=0)
    
    # 터미널 출력
    print("Soil Moisture: {:.2f}%".format(moisture_percentage))
    
    # 1초 대기
    sleep(1)