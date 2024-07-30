# Run this program for the 'Real-Time Chat' to work.
# Imports
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Message

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
socketio = SocketIO(app)
@app.route('/')

# Defining index
def index():
    return render_template('index.html')

@socketio.on('send_message')

# Defining how to handle sent message
def handle_send_message(data):
    username = data['username']
    text = data['text']
    message = Message(username=username, text=text)
    db.session.add(message)
    db.session.commit()
    emit('receive_message', {'username': username, 'text': text, 'timestamp': str(message.timestamp)}, broadcast=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
