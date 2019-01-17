# Web server
from flask import Flask, render_template, request
from flask_socketio import SocketIO

# MiMo
from mimo.hardware.io import buttons, button_leds, button_states, lcd_screens
from mimo.utils import I2C_LCD_driver

# GPIO
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '1Secret!'
socketio = SocketIO(app)


def emit(data):
    socketio.emit('gpio', data)


def button_callback(channel):
    print(channel)
    if button_states[channel]:
        emit('gpio', {'action': buttons[channel]})


def init_hardware():
    GPIO.setmode(GPIO.BOARD)

    # Init buttons
    for pin in buttons.keys():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=1000)

    # Init button LEDs
    for pin in button_leds.keys():
        GPIO.setup(pin, GPIO.OUT)

    # Init lcd screens
    for k, v in lcd_screens.items():
        lcd_screens[k]['instance'] = I2C_LCD_driver.lcd(v['address'])


def init_test():
    for k, v in buttons.items():
        data = {'action': v}
        emit(data)
        socketio.sleep(1)


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


@socketio.on('btn_set_state')
def btn_set_state(json_data, methods=['GET', 'POST']):
    btn_id = int(json_data['btn_id'])
    btn_state = bool(json_data['btn_state'])

    # Change button state
    button_states[btn_id] = btn_state


@socketio.on('btn_led')
def btn_led(json_data, methods=['GET', 'POST']):
    btn_led_id = int(json_data['btn_led_id'])
    btn_led_state = bool(json_data['btn_led_state'])

    if btn_led_state is True:
        GPIO.output(btn_led_id, GPIO.HIGH)
    else:
        GPIO.output(btn_led_id, GPIO.LOW)


if __name__ == '__main__':
    init_hardware()
    socketio.run(app, host='0.0.0.0', port='8000', debug=True)
