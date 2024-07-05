from picozero import DHTSensor
from time import sleep, localtime

#localtime() 의 튜플 값은
#(연도, 달, 날, 시간, 분, 초, 요일[일~토/0~6], 1월1일부터 경과한 일 수)
start_time=localtime() #측정 시작시간 확인
print(start_time)

dht_sensor = DHTSensor(pin=0, model='DHT11')

f = open('temp002.csv', 'w') #피코 파일 경로랑 같이 있어야함
f.write(f'Time,Temperature,Humidity\n')#시간,분,초를 한줄에 입력받을 때
f.write(f'Hour,Min,Second,Temperature,Humidity\n')#시간,분,초를 따로 입력 받을 때

#1시간 측정을 기준
while True:
    temp=dht_sensor.temperature
    print(temp)
    sleep(0.5)
    
    humi = dht_sensor.humidity
    print(humi)
    sleep(0.5)

    cur_time=localtime() #현재시각 측정
    #시간,분,초를 한줄로
    #f.write(f'{cur_time[3]}:{cur_time[4]}:{cur_time[5]},{temp},{humi}\n')
    #시간,분,초를 따로 입력받을 때
    f.write(f'{cur_time[3]},{cur_time[4]},{cur_time[5]},{temp},{humi}\n')

end_time=localtime() #측정 종료시간 확인
f.write(f'{end_time}\n')
f.close()

