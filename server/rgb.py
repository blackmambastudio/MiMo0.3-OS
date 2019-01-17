import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RED = 16
GREEN = 18
BLUE = 22

GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, 0)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(GREEN, 0)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(BLUE, 0)

try:
    while True:
        GPIO.output(RED, int(1001))
        GPIO.output(GREEN, int(010))
        GPIO.output(BLUE, int(001))
except KeyboardInterrupt:
    GPIO.cleanup()
