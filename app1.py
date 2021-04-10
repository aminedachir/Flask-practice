from flask import Flask 
app1 = Flask(__name__)


@app1.route("/")
def index():
	return "<h1>Hello, ther</h1>"


@app1.route("/user/<name>")
def home(name):
	return "hello, %s"%name

if __name__ == '__main__':
	app1.run(port = 4500, debug = True)
