from flask import Flask, request, render_template
import time
from datetime import datetime

app = Flask(__name__)

def time_format(t):
  return datetime.fromtimestamp(t)

all_messages = [
  {
    'text': 'test message',
    'name': 'username',
    'time': time_format(time.time() - 3600)
  }
]

@app.route('/')
def root():
  return 'HOME PAGE'

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route('/get_messages')
def get_messages():
  return {'messages': all_messages}

@app.route('/send')
def send_message():
  text = request.args['text']
  name = request.args['name']

  if len(name) < 3 or len(name) > 100:
        return 'ERROR: name'
  
  if len(text) < 1 or len(text) > 3000:
        return 'ERROR: text'

  message = {
    'text': text,
    'name': name,
    'time': time_format(time.time())
  }

  all_messages.append(message)

  return 'OK'

app.run()