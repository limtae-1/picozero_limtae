from picozero import Buzzer
#from picozero import Buzzer
from time import sleep
'''
buzzer = Buzzer(15)

buzzer.on()   #소리를 키는 명령어
sleep(1)
buzzer.off()  #소리를 끄는 명령어
sleep(1)

buzzer.beep() #소리를 지속하는 명령어
sleep(4)
buzzer.off()
'''

buzzer = Buzzer(15)

buzzer.on()   #소리를 키는 명령어
sleep(0.5)
buzzer.off()  #소리를 끄는 명령어
sleep(1)

#buzzer.beep() #소리를 지속하는 명령어
#sleep(4)
#buzzer.off()