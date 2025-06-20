from picozero import PhotoInterrupter
from time import sleep

photo = PhotoInterrupter(14)  # 포토인터럽터 핀

while True:
    if photo.is_blocked():
        print("🚧 포토인터럽터: 물체 감지!")
        sleep(0.5)
    else:
        print("🚧 포토인터럽터: 물체가 없습니다.!")
        sleep(0.5)
