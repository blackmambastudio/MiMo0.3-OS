import RPi.GPIO as IO

IO.setmode(IO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
