from app import app 
from app import socketio, emit, render_template

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('connected')
def initial_greeting():
    emit('greeting', "Hey, what's up, friend old")