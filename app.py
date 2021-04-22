from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(db, app)


@app.route('/')
def home():
	return "hello"

if __name__ == '__main__':
	app.run()

















