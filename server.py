#!/usr/bin/env python3

from flask import Flask
from flask import request

import urllib.request
import json

# Import from the 21 Bitcoin Develper Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# Configure the app
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

API_URL = 'http://api.icndb.com/jokes/random'

@app.route('/joke')
@payment.required(1000)
def joke():
  response = urllib.request.urlopen(API_URL).read()
  response = response.decode('utf-8')
  joke = json.loads(response)['value']['joke']
  return joke 

@app.route('/')
@app.route('/info')
def get_info():
  info = {"name": "Chuck Norris Joke Service"}
  body = json.dumps(info)
  return (body, 200, {
    'Content-length': len(body),
    'Content-type': 'application/json'
  })

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
