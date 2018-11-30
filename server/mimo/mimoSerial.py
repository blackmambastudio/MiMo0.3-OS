import RPi.GPIO as GPIO


def action():
    print('Callback from pi')
    socket.emit(-action1)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(4, GPIO.BOTH)

init()

GPIO.add_event_callback(4, action)
GPIO.add_event_callback(5, action2)
