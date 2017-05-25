import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# FITBIT_CLIENT_ID = os.environ.get('FITBIT_CLIENT_ID')
# FITBIT_CLIENT_SECRET = os.environ.get('FITBIT_CLIENT_SECRET')
# SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

with open("app_details.txt") as text:
    details = text.read().split()
    FITBIT_CLIENT_ID = details[0]
    FITBIT_CLIENT_SECRET = details[1]

    text.close()
