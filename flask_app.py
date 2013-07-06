import sqlite3
from contextlib import closing
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

# method to connect to db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# initialize the db
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# run the server
if __name__ == '__main__':
    app.run()