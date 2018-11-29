from flask import Flask, render_template
from flask_socketio import SocketIO
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'
socketio = SocketIO(app)


@app.route('/')
def index():
    render_template('index.html')


def handle_serial(methods=['GET', 'POST']):
    print('Received from serial IO')


@socketio.on('connect2pi')
def serial_read(json_data, methods=['GET', 'POST']):
    """
    Reads from serial and emits to WS event
    TODO: Read data from Pi inputs
    """
    print('Connected from {0}'.format(json_data))
    response = {'message': 'Connected to serial'}
    socketio.emit('serial', response, callback=serial_read)

    # Test if WS is working
    data = {'type': 'serial_input', 'data': 'Hello from serial'}
    while True:
        socketio.emit('serial', data, callback=serial_read)
        # Sleep for 10 seconds
        time.sleep(10)











