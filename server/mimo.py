from flask import Flask, render_template
from flask_socketio import SocketIO
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


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

    # Sleep for 5 seconds
    time.sleep(5)
    socketio.emit('serial', response, callback=handle_serial)

    # Test if WS is working
    data = {'type': 'serial_input', 'data': 'hello'}

    # TODO: Implement serial read here
    while True:
        socketio.emit('serial', data, callback=handle_serial)

        # Sleep for 10 seconds
        time.sleep(10)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
