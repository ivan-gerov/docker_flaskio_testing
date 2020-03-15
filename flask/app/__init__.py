from flask import Flask, render_template
from flask import Blueprint, Flask, current_app, render_template, session
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top_secret!'

socketio = SocketIO(app)


from app import views
