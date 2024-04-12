from flask import Flask,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from utils import *

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app = app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/getall')

def hello_world():
    x = get_all()
    return jsonify([{'id': i.id, 'username': i.username} for i in x])

@app.route('/add/<username>')
def add_user(username):
    x = add(username)
    return f'User added: {x.id}: {x.username}'