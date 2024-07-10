from picozero import I2C_LCD
from time import sleep

# I2C LCD 디스플레이 설정 (SCL=5, SDA=4 핀 사용)
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