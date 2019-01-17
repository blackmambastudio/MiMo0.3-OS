from flask import Flask, render_template, request
from flask_socketio import SocketIO

from mimo.hardware.io import lcd_screens
from mimo.utils import I2C_LCD_driver


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

def init_hardware():
    for k, v in lcd_screens.items():
        lcd_screens[k]['instance'] = I2C_LCD_driver.lcd(lcd_screens[k]['address'])

def lcd_display_message(lcd_id, message, line):
    lcd_screens[lcd_id]['instance'].lcd_display_string(message, line)


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

    data = {
        'action': action
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

@socketio.on('lcd_print')
def lcd_print(json_data, methods=['GET', 'POST']):
    lcd_id = int(json_data['lcd_id'])
    message = json_data['message']
    line = int(json_data['line'])

    # Print to lcd screen
    lcd_display_message(lcd_id, message, line)

@socketio.on('lcd_clear')
def lcd_clear(json_data, methods=['GET', 'POST']):
    lcd_id = int(json_data['lcd_id'])
    
    # Clear LCD screen
    lcd_screens[lcd_id]['instance'].lcd_clear()

@socketio.on('connect2pi')
def handle_serial(json_data, methods=['GET', 'POST']):
    print('Connected from {0}'.format(json_data))
    data = {'message': 'Connected to serial'}
    socketio.emit('serial', data, callback=serial_read)


if __name__ == '__main__':
    init_hardware()
    socketio.run(app, host='0.0.0.0', port='8000', debug=True)
