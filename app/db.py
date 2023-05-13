from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or ''
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or '127.0.0.1' # localhost
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'flaskcontacts'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DB']}"



# MySQL Connection
mysql = MySQL(app)
