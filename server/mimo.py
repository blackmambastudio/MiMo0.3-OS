from flask import Flask, render_template
from flask_socketio import SocketIO


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
    print('Connected from {0}'.format(json_data))
    response = {'message': 'Connected to serial'}










