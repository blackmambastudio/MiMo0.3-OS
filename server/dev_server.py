from flask import Flask, render_template, request
from flask_socketio import SocketIO

from mimo.hardware.io import buttons, button_states


app = Flask(__name__)
app.config['SECRET_KEY'] = '1Secret!'
socketio = SocketIO(app)


def emit(data):
    socketio.emit('gpio', data)


def init_test():
    while True:
        for k, v in buttons.items():
            data = {'action': v}
            emit(data)
            socketio.sleep(1)
        break
    return


def display_lcd(i2c_address, message):
    screens[i2c_address].lcd_display_string(message, 1)


@app.route('/test')
def index():
    return render_template('test.html')


@app.route('/emulator')
def emulator():
    return render_template('emulator.html')


@app.route('/screen')
def screen():
    return render_template('screen.html')


@app.route('/gpio/')
def web_gpio():
    action = request.args.get('action')
    status = request.args.get('status')

    data = {
        'action': action,
        'status': status
    }

    if action == 'ON':
        data = {'action': 'MiMo Console is starting up...'}
        emit(data)
        init_test()
    else:
        emit(data)
    return "ok"


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
