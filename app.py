from flask import Flask, request
from driver import getMessengerScreenshot
app = Flask(__name__)

@app.route('/')
def index():
  name = request.args['name']
  print("name: " + name)
  getMessengerScreenshot(name)
  return 'Took screenshot!'