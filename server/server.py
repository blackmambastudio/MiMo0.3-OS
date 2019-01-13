from flask import Flask, render_template, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = '1Secret!'
socketio = SocketIO(app)


def emit(data):
    socketio.emit('gpio', data, callback=serial_read)


@app.route('/gpio/')
def web_gpio():
    button = request.args.get('button')
    data = {
        'button': button
    }
    emit(data)
    return render_template('gpio.html', button=button)


def messageReceived(methods=['GET', 'POST']):
    print('Message received')


def serial_read(methods=['GET', 'POST']):
    print('Message received serial')


@socketio.on('connect2pi')
def handle_serial(json_data, methods=['GET', 'POST']):
    print('Connected from {0}'.format(json_data))
    data = {'message': 'Connected to serial'}
    socketio.emit('serial', data, callback=serial_read)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='8000', debug=True)
