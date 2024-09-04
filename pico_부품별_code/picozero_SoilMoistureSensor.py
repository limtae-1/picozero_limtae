from picozero import SoilMoistureSensor
from time import sleep


'''
#아래 코드는 습도를 0~100%로 표현하는 코드
#0은 건조에 가까운 것 100%습함에 가까운 것
sensor = SoilMoistureSensor(pin=26, min_value=20000, max_value=50000)

while True:
    moisture_percentage = sensor.read_percentage()
    print("Soil Moisture: {:.2f}%".format(moisture_percentage))
    
    sleep(1)

class SoilMoistureSensor:
    def __init__(self, pin, min_value=20000, max_value=50000):
        self.adc = ADC(Pin(pin))  # 아날로그 핀 설정
        self.min_value = min_value  # 최소 센서 값 (건조한 상태)
        self.max_value = max_value  # 최대 센서 값 (습한 상태)

    def read_raw_value(self):
        # ADC 값을 읽어옴
        return self.adc.read_u16()

    def read_percentage(self):
        # 센서 값을 퍼센트(%)로 변환
        raw_value = self.read_raw_value()
        # 퍼센트로 변환하여 반환 (0% - 100%)
        percentage = (raw_value - self.min_value) / (self.max_value - self.min_value) * 100
        return max(0, min(100, percentage))  # 0%에서 100% 범위로 제한
'''

#===========경계선===========
'''
#같이 써야하는 클래스도 정의함.
#아래 코드는 습도를 0~1로만 표현
#0은 건조에 가까운 것 1은 습함의 가까운 정도

sensor = SoilMoistureSensor(pin=26, threshold=0.4)

while True:
    moisture_level = sensor.read_value()
    if sensor.is_soil_moist():
        print("Soil is moist:", moisture_level)
    else:
        print("Soil is dry:", moisture_level)
    sleep(1)
    
    
class SoilMoistureSensor:
    def __init__(self, pin, threshold=0.5):
        self.adc = ADC(Pin(pin))  # 아날로그 핀 설정
        self.threshold = threshold  # 임계값 설정

    def read_value(self):
        # ADC 값을 0.0에서 1.0 사이의 값으로 변환
        return self.adc.read_u16() / 65535

    def is_soil_moist(self):
        # 토양이 임계값보다 습한지 여부 확인
        return self.read_value() > self.threshold

    def set_threshold(self, threshold):
        # 임계값 설정
        self.threshold = threshold
'''