from picozero import DHTSensor
from time import sleep, localtime

#localtime() 의 튜플 값은
#(연도, 달, 날, 시간, 분, 초, 요일[일~토/0~6], 1월1일부터 경과한 일 수)
start_time=localtime()
print(start_time)

dht_sensor = DHTSensor(pin=0, model='DHT11')

f = open('test002.csv', 'w') #피코 파일 경로랑 같이 있어야함
f.write(f'{start_time}\n')

#1시간 측정을 기준
for i in range(3600):
    temp=dht_sensor.temperature
    print(temp)
    sleep(1)
    
    humi = dht_sensor.humidity
    print(humi)
    sleep(1)

    #real_time=localtime()
    #f.write("%s" f'{real_time}\n' %data)
    f.write("%d %d" %(temp,humi))
    f.write("\n")
    

end_time=localtime()
f.write(f'{end_time}\n')
f.close()

