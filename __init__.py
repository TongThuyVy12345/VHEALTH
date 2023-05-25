from flask import Flask
from flask_admin import Admin
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

