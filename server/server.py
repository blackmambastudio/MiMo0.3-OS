# MiMo imports
from flask import Flask, render_template
from flask_socketio import SocketIO

# MiMo dependencies
from mimo.hardware.io import buttons, button_states, lcd_screens
from mimo.utils import I2C_LCD_driver

# GPIO dependencies
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '1Secret!'
socketio = SocketIO(app)


def emit(data):
    socketio.emit('gpio', data, callback=serial_read)


def button_callback(channel):
    if button_states[channel]:
        emit('gpio', {'button': buttons[channel]})


def init_hardware():
    GPIO.setmode(GPIO.BOARD)

    # Init buttons
    for pin in buttons.keys():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=1000)

    # Init lcd screens
    for pin in lcd_screens.keys():
        hex_pin = hex(int(pin, 16))
        lcd_screens[pin] = I2C_LCD_driver.lcd(hex_pin)


def init_test():
    for k, v in buttons.items():
        data = {'action': v}
        emit(data)
        socketio.sleep(1)
    return


def serial_read(methods=['GET', 'POST']):
    print('Message received serial')


def display_lcd(i2c_address, message):
    lcd_screens[i2c_address].lcd_display_string(message, 1)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect2pi')
def handle_serial(json_data, methods=['GET', 'POST']):
    print('Connected from {0}'.format(json_data))
    data = {'message': 'Connected to serial'}
    socketio.emit('serial', data, callback=serial_read)


@socketio.on('gpio')
def gpio(json_data, methods=['GET', 'POST']):
    # TODO
    pass


if __name__ == '__main__':
    # Initialize MiMo Console
    init_test()
    init_hardware()
    socketio.run(app, host='0.0.0.0', port='8000', debug=True)
