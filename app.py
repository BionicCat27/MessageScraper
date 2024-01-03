from flask import Flask, request, send_file
from driver import getMessengerScreenshot
app = Flask(__name__)

@app.route('/')
def index():
  name = request.args['name']
  print("name: " + name)
  filename = getMessengerScreenshot(name)
  return send_file(filename, mimetype='image/png')