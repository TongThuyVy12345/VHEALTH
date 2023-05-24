from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.secret_key = 'your_secret_key'


