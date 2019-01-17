import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RED = 16
GREEN = 18
BLUE = 22

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.cleanup()

def set_color(a, b, c):
    GPIO.output(GREEN, a)
    GPIO.output(RED, b)
    GPIO.output(BLUE, c)

try:
    while True:
        GPIO.output(RED, int(1 ))
        GPIO.output(GREEN, int(0))
        GPIO.output(BLUE, int(0))

except KeyboardInterrupt:
    GPIO.cleanup()
