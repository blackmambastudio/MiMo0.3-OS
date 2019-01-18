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

# GPIO.setup(27, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

buttons = OrderedDict()
buttons[12] = {'msg': 'BTN-A', 'state': True}
buttons[16] = {'msg': 'BTN-B', 'state': True}
buttons[18] = {'msg': 'BTN-C', 'state': True}
buttons[22] = {'msg': 'BTN-D', 'state': True}
buttons[24] = {'msg': 'BTN-E', 'state': True}
buttons[26] = {'msg': 'BTN-F', 'state': True}


while True:
    time.sleep(0.5)
    if GPIO.input(12) == GPIO.HIGH:
        print(12)
        if buttons[12]['state']:
            GPIO.output(12, GPIO.HIGH)
            buttons[12]['state'] = False
        else:
            GPIO.output(12, GPIO.LOW)
            buttons[12]['state'] = True

    if GPIO.input(16) == GPIO.HIGH:
        print(16)
        if buttons[16]['state']:
            GPIO.output(16, GPIO.HIGH)
            buttons[16]['state'] = False
        else:
            GPIO.output(16, GPIO.LOW)
            buttons[16]['state'] = True
    if GPIO.input(18) == GPIO.HIGH:
        print(18)
        if buttons[18]['state']:
            GPIO.output(18, GPIO.HIGH)
            buttons[18]['state'] = False
        else:
            GPIO.output(18, GPIO.LOW)
            buttons[18]['state'] = True
    if GPIO.input(22) == GPIO.HIGH:
        print(22)
        if buttons[22]['state']:
            GPIO.output(22, GPIO.HIGH)
            buttons[22]['state'] = False
        else:
            GPIO.output(22, GPIO.LOW)
            buttons[22]['state'] = True
    if GPIO.input(24) == GPIO.HIGH:
        print(24)
        if buttons[24]['state']:
            GPIO.output(24, GPIO.HIGH)
            buttons[24]['state'] = False
        else:
            GPIO.output(24, GPIO.LOW)
            buttons[24]['state'] = True
    if GPIO.input(26) == GPIO.HIGH:
        print(26)
        if buttons[26]['state']:
            GPIO.output(26, GPIO.HIGH)
            buttons[26]['state'] = False
        else:
            GPIO.output(26, GPIO.LOW)
            buttons[26]['state'] = True
