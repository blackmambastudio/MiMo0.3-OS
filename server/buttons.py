import RPi.GPIO as GPIO
import time
from collections import OrderedDict

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


buttons = OrderedDict()
buttons[12] = {'msg': 'BTN-A', 'state': True}
buttons[16] = {'msg': 'BTN-B', 'state': True}
buttons[18] = {'msg': 'BTN-C', 'state': True}
buttons[22] = {'msg': 'BTN-D', 'state': True}
buttons[24] = {'msg': 'BTN-E', 'state': True}
buttons[26] = {'msg': 'BTN-F', 'state': True}


while True:
    time.sleep(1)
    if GPIO.input(12) == GPIO.HIGH:
        print(12)
        if 
    if GPIO.input(16) == GPIO.HIGH:
        print(16)
    if GPIO.input(18) == GPIO.HIGH:
        print(18)
    if GPIO.input(22) == GPIO.HIGH:
        print(22)
    if GPIO.input(24) == GPIO.HIGH:
        print(24)
    if GPIO.input(26) == GPIO.HIGH:
        print(26)
