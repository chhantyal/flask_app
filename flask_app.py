import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# configuration
DATABASE = '/tmp/flask_app.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# application
app = Flask(__name__)
app.config.from_object(__name__)