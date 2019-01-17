# MiMo imports
from flask import Flask, render_template
from flask_socketio import SocketIO

# MiMo dependencies
from mimo.hardware.io import buttons, button_states#, lcd_screens
#from mimo.utils import I2C_LCD_driver

# GPIO dependencies
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '1Secret!'
socketio = SocketIO(app)


def emit(data):
    socketio.emit('gpio', data, callback=serial_read)


def blink_led(led):
    print(led)

button_status = {
    12: False,
    16: False
}

def button_callback(channel):
    print "entra evento channel " + str(channel)
    if button_states[channel]:
        print "button available channel " + str(channel) + " -> " + str(GPIO.input(channel))
        button_status[channel] = not button_status[channel]
        if button_status[channel]:
            print 'on pressed'
            socketio.emit('gpio', {'button': buttons[channel], 'status': 1})
        else:
            print 'on release'
            socketio.emit('gpio', {'button': buttons[channel], 'status': 0})
        #if GPIO.input(channel):
        #print "pressed"
        #socketio.emit('gpio', {'button': buttons[channel]})
        #blink_led(channel)


def init_hardware():
    GPIO.setmode(GPIO.BOARD)

    # Init buttons
    for pin in buttons.keys():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=button_callback, bouncetime=10)

    # Init lcd screens
    #for k, v in lcd_screens.items():
    #    lcd_screens[k]['instance'] = I2C_LCD_driver.lcd(v['address'])


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
