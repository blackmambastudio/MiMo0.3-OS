import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print(7)
    if GPIO.input(11) == GPIO.HIGH:
        print(11)
    if GPIO.input(13) == GPIO.HIGH:
        print(13)
    if GPIO.input(15) == GPIO.HIGH:
        print(15)
    if GPIO.input(19) == GPIO.HIGH:
        print(19)
    if GPIO.input(21) == GPIO.HIGH:
        print(21)


