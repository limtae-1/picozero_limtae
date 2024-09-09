from time import sleep
from picozero import Neopixel

# 핀 번호와 네오픽셀 LED 개수를 설정
pin_num = 15  # 네오픽셀을 연결한 GPIO 핀 번호
num_leds = 10  # 제어할 네오픽셀 LED 개수

# PicoNeoPixel 객체 생성
neopixel_strip = Neopixel(pin=pin_num, num_leds=num_leds)

# 예시: 모든 LED를 빨간색으로 설정
neopixel_strip.fill((255, 255, 0))
neopixel_strip.show()
sleep(3)

neopixel_strip.clear()
# 예시: 특정 LED만 파란색으로 설정 (2번째 LED)
neopixel_strip.set_pixel(9, (0, 0, 255))
neopixel_strip.show()
sleep(3)

# 예시: 모든 LED 끄기
neopixel_strip.clear()
#neopixel_strip.show()