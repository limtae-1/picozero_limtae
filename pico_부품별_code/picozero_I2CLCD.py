from picozero import I2C_LCD
from time import sleep

# I2C LCD 디스플레이 설정 (SCL=5, SDA=4 핀 사용)
# I2C LCD 디스플레이 통신속도 조절 가능 lcd = I2C_LCD(scl=5, sda=4, freq=1000000) 이처럼 파라미터에 freq 속성을 추가하면됨 굳이,, 조절할 필욘 없을듯)
# LCD 디스플레이에 띄울 땐 문자형자료형으로 변환하여 띄우는 것에 주의할 것 !
# 글씨가 깨져서 나오는 경우는 sleep()명령어를 통해 약간의 딜레이를 주면 해결됨
# clear()명령어 앞에 sleep 붙이기
lcd = I2C_LCD(scl=5, sda=4)

# LCD 초기화
lcd.clear()

# 첫 번째 줄에 텍스트 출력
lcd.putstr('Hello, World!', col=0, row=1)

# 두 번째 줄에 텍스트 출력
lcd.putstr(a, col=0, row=0)

# 백라이트 끄기
sleep(2)
lcd.backlight_off()

# 1초 대기
sleep(1)

# 백라이트 켜기
lcd.backlight_on()


