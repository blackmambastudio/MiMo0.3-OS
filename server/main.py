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
