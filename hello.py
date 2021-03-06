import os
from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
	logging.debug("saying hello heroku!")
	name = os.environ.get('NAME','DreamForceXXXX')
	return 'Hello %s!' % name