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


try:
    while True:
        if GPIO.input(16) == GPIO.HIGH and buttons[16]['state']:
            print('16')
            GPIO.output(29, GPIO.HIGH)
            buttons[16]['state'] = False
        elif not(GPIO.input(16) == GPIO.HIGH and buttons[16]['state']):
            GPIO.output(29, GPIO.LOW)
            buttons[16]['state'] = True

        if GPIO.input(24) == GPIO.HIGH and buttons[24]['state']:
            print('24')
            GPIO.output(35, GPIO.HIGH)
            buttons[24]['state'] = False
        elif not(GPIO.input(24) == GPIO.HIGH and buttons[24]['state']):
            GPIO.output(35, GPIO.LOW)
            buttons[24]['state'] = True

        # if GPIO.input(18) == GPIO.HIGH:
        #     print(18)
        #     if buttons[18]['state']:
        #         GPIO.output(31, GPIO.HIGH)
        #         buttons[18]['state'] = False
        #     else:
        #         GPIO.output(31, GPIO.LOW)
        #         buttons[18]['state'] = True
        # if GPIO.input(22) == GPIO.HIGH:
        #     print(22)
        #     if buttons[22]['state']:
        #         GPIO.output(33, GPIO.HIGH)
        #         buttons[22]['state'] = False
        #     else:
        #         GPIO.output(33, GPIO.LOW)
        #         buttons[22]['state'] = True
        # if GPIO.input(24) == GPIO.HIGH:
        #     print(24)
        #     if buttons[24]['state']:
        #         GPIO.output(35, GPIO.HIGH)
        #         buttons[24]['state'] = False
        #     else:
        #         GPIO.output(35, GPIO.LOW)
        #         buttons[24]['state'] = True
        # if GPIO.input(26) == GPIO.HIGH:
        #     print(26)
        #     if buttons[26]['state']:
        #         GPIO.output(37, GPIO.HIGH)
        #         buttons[26]['state'] = False
        #     else:
        #         GPIO.output(37, GPIO.LOW)
        #         buttons[26]['state'] = True
except KeyboardInterrupt:
    GPIO.cleanup()
