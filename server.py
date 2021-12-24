from flask import Flask, request, render_template
import time
from datetime import datetime
import json

app = Flask(__name__)

messages_file = './data/messages.json'
json_file = open(messages_file, 'rb')
data = json.load(json_file)

if not 'all_messages' in data:
  print(f'Can not find all_messages in {messages_file}')
  exit(1)
  
all_messages = data['all_messages']

def save_messages():
  data = {
    'all_messages': all_messages
  }
  json_file = open(messages_file, 'w')
  json.dump(data, json_file)

def time_format(t):
  return str(datetime.fromtimestamp(t))

@app.route('/')
def root():
  return 'HOME PAGE'

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route('/get_messages')
def get_messages():
  return {'all_messages': all_messages}

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
  save_messages()

  return 'OK'

app.run()