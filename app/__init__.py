from flask import Flask

# FLASK
# Inicia la aplicació
app = Flask(__name__)
app.config.from_object("config.TestingConfig")

from app import utils, routes
