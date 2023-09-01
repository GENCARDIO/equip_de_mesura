from flask import Flask

# FLASK
# Inicia la aplicació
app = Flask(__name__)
app.secret_key = "12345"
app.config.from_object("config.Config_Arxius")

from app import utils, routes
