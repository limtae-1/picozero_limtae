from picozero import DistanceSensor
from time import sleep

ds = DistanceSensor(echo=20, trigger=21) #거리측정 코드
f=open("test04.csv", 'w', encoding='utf-8')

while True:
    dscm = ds.distance * 100 #cm로 바꿔주기 위한 코드
    print(dscm)
    sleep(0.2)
    for i in range(1,11):
        data = str(dscm)
        f.write('\n'.join(data))
        
f.close()
'''
#파일생성
#파일객체=open(파일이름, 파일 열기모드)
f=open("test03.csv", 'w', encoding='utf-8')
#f=open("c:/경로/경로/파일명.확장자", "권한")
#r=읽기 모드
#w=쓰기 모드
#a=추가 모드
for i in range(1,11):
    data = "%d번쨰 줄입니다.\n" %i
    f.write(data)


f.close()
'''

'''
with 문의 역할 : 파일을 열면(open) 항상 닫아(close)주어야 한다.
파일을 여닫는 것을 자동으로 처리하면 좋음 !
with문이 이 역할을 해줌 with 블록을 벗어나는 순간 파일 객체 f가 자동으로 닫힘
ex)
with open("test.csv", "w") as f:
    f.write("Life is too short, you need python")
'''
'''
data = [
    ['ultra', 'temp', 'led'],
    ['dscm', '2', '3'],
    ['4', '5', '6']
]

with open('test03.csv', 'w') as file:
    for row in data:
        file.write(','.join(row) + '\n')
        
print("hello")

'''




