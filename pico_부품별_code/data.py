from picozero import DistanceSensor
from time import sleep, localtime

#localtime() 의 튜플 값은
#(연도, 달, 날, 시간, 분, 초, 요일[일~토/0~6], 1월1일부터 경과한 일 수)
start_time=localtime()
print(start_time)

ds = DistanceSensor(echo=20, trigger=21) #거리측정 코드

f = open('test047.csv', 'w') #피코 파일 경로랑 같이 있어야함
f.write(f'{start_time}\n')

#1시간 측정을 기준
for i in range(3600):
    dscm=ds.distance * 100
    print(dscm)
    sleep(1)
    if dscm<100:
        real_time=localtime()
        data=str(dscm)
        #f.write("%s" f'{real_time}\n' %data)
        f.write(f'{real_time}\n')
        f.write("%s\n" %data)
    else:
        continue

end_time=localtime()
f.write(f'{end_time}\n')
f.close()






'''
#====== 아래는 여러개 속성을 입력할 때 참고할 것 ======
# CSV 파일 쓰기
data = [
    ['열1', '열2', '열3'],
    ['데이터1', '데이터2', '데이터3'],
    ['데이터4', '데이터5', '데이터6']
]

with open('출력파일.csv', 'w') as file:
    for row in data:
        file.write(','.join(row) + '\n')

'''