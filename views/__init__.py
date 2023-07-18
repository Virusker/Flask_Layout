from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os,sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # Thêm đường dẫn của thư mục gốc vào sys.path
# sys.path.append(base_dir)

app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config.from_pyfile('../config.py')

#db = SQLAlchemy(app=app)

from views.index import index_bp
app.register_blueprint(index_bp)
