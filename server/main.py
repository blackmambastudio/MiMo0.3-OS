from flask import Flask, render_template
from flask_socketio import SocketIO
import time
from mimo.core import mimo_button
# from mimo.utils import I2C_LCD_driver
from mimo.events import EventBus

# from mimo.mimoSerial import *
# from mimo.mimoPrinter import mimo_print, mimo_setup, mimo_init
# import RPi.GPIO as GPIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'
socketio = SocketIO(app)

# RGB LED Setup
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xFFFFFF, 0x9400D3]
pins = {'pin_R': 11, 'pin_G': 12, 'pin_B': 13}  # pins is a dict

# Setup Pi IO for buttons
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup LCD screens
# lcd21 = I2C_LCD_driver.lcd(0x21)
# lcd22 = I2C_LCD_driver.lcd(0x22)
# lcd23 = I2C_LCD_driver.lcd(0x23)
# lcd25 = I2C_LCD_driver.lcd(0x25)
# lcd26 = I2C_LCD_driver.lcd(0x26)
# lcd27 = I2C_LCD_driver.lcd(0x27)

# SCREENS = {
#     21: lcd21,
#     22: lcd22,
#     23: lcd23,
#     25: lcd25,
#     26: lcd26,
#     27: lcd27
# }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


def handle_serial(methods=['GET', 'POST']):
    print('Received from serial IO')


def handle_button(channel):
    data = {}
    socketio.emit('gpio', data)


# def display_lcd(i2c_address, message):
#     SCREENS[i2c_address].lcd_display_string(message, 1)


# def setup_pi():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#     GPIO.add_event_detect(4, GPIO.BOTH)

#     # Setup LED
#     for i in pins:
#         GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
#         GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led

#     p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
#     p_G = GPIO.PWM(pins['pin_G'], 2000)
#     p_B = GPIO.PWM(pins['pin_B'], 2000)

#     p_R.start(0)      # Initial duty Cycle = 0(leds off)
#     p_G.start(0)
#     p_B.start(0)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# def setColor(col):   # For example : col = 0x112233
#     R_val = (col & 0x110000) >> 16
#     G_val = (col & 0x001100) >> 8
#     B_val = (col & 0x000011) >> 0

#     R_val = map(R_val, 0, 255, 0, 100)
#     G_val = map(G_val, 0, 255, 0, 100)
#     B_val = map(B_val, 0, 255, 0, 100)

#     p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
#     p_G.ChangeDutyCycle(100-G_val)
#     p_B.ChangeDutyCycle(100-B_val)


@socketio.on('connect2pi')
def serial_read(json_data, methods=['GET', 'POST']):
    """
    Reads from serial and emits to WS event
    TODO: Read data from Pi inputs
    """

    # Init printer
    # mimo_init()

    # Setup connection with PI
    print('Connected from {0}'.format(json_data))
    response = {'message': 'Connected to serial'}

    # Sleep for 5 seconds
    time.sleep(5)
    socketio.emit('serial', response, callback=handle_serial)

    # Test if WS is working
    data = {'type': 'serial_input', 'data': 'hello', 'button': ''}

    cable = {
        'user': 'MiMo Console',
        'date': 'Oct 30  1982',
        'text': 'I saw the best minds of my generation destroyed by madness...'
    }

    # TODO: Implement serial read here
    while True:
        # Setup printer to print at will
        # mimo_setup()

        # Print
        # mimo_print(cable)

        data['button'] = mimo_button()
        socketio.emit('serial', data, callback=handle_serial)

        # Sleep for 10 seconds
        time.sleep(10)


if __name__ == '__main__':
    # Add button events
    # GPIO.add_event_detect(12, GPIO.RISING, callback=handle_button, bouncetime=1000)
    # GPIO.add_event_detect(16, GPIO.RISING, callback=handle_button, bouncetime=1000)
    # GPIO.add_event_detect(18, GPIO.RISING, callback=handle_button, bouncetime=1000)
    # GPIO.add_event_detect(22, GPIO.RISING, callback=handle_button, bouncetime=1000)
    # GPIO.add_event_detect(32, GPIO.RISING, callback=handle_button, bouncetime=1000)
    # GPIO.add_event_detect(36, GPIO.RISING, callback=handle_button, bouncetime=1000)

    socketio.run(app, host='0.0.0.0', debug=True)
