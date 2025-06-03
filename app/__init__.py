import os
from flask import Flask
from flask_cors import CORS

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir   = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

from app.routes import views
