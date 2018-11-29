from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'
socketio = SocketIO(app)


@app.route('/')
def index():
    render_template('index.html')
