from flask import Flask, render_template
from flask_socketio import SocketIO
import time
from mimo.core import mimo_button
from mimo.mimoSerial import *
import RPi.GPIO as GPIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'
socketio = SocketIO(app)

# RGB LED Setup
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xFFFFFF, 0x9400D3]
pins = {'pin_R': 11, 'pin_G': 12, 'pin_B': 13}  # pins is a dict


@app.route('/')
def index():
    return render_template('index.html')


def handle_serial(methods=['GET', 'POST']):
    print('Received from serial IO')


def setup_pi():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(4, GPIO.BOTH)

    # Setup LED
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
        GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led

    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 2000)
    p_B = GPIO.PWM(pins['pin_B'], 2000)

    p_R.start(0)      # Initial duty Cycle = 0(leds off)
    p_G.start(0)
    p_B.start(0)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setColor(col):   # For example : col = 0x112233
    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
    p_G.ChangeDutyCycle(100-G_val)
    p_B.ChangeDutyCycle(100-B_val)


@socketio.on('connect2pi')
def serial_read(json_data, methods=['GET', 'POST']):
    """
    Reads from serial and emits to WS event
    TODO: Read data from Pi inputs
    """

    # Setup connection with PI
    print('Connected from {0}'.format(json_data))
    response = {'message': 'Connected to serial'}

    # Sleep for 5 seconds
    time.sleep(5)
    socketio.emit('serial', response, callback=handle_serial)

    # Test if WS is working
    data = {'type': 'serial_input', 'data': 'hello', 'button': ''}

    # TODO: Implement serial read here
    while True:
        data['button'] = mimo_button()
        socketio.emit('serial', data, callback=handle_serial)

        # Sleep for 10 seconds
        time.sleep(10)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
