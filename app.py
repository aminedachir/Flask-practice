from flask import Flask 
from SQL

app = Flask(__name__)

db = SQL("sqlite:///app.db")

@app.route('/')
def home():
	return "hello"

if __name__ == '__main__':
	app.run()

















