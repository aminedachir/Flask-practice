from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hom():
   return render_template('Welcome.html')

@app.route("/Division")
def dv():
   return render_template('Division.html')

@app.route("/summation")
def home():
   return render_template('summation.html')

@app.route("/multiplication")
def homes():
   return render_template('multiplication.html')

@app.route("/Conversion")
def js():
   return render_template('js.html')

if __name__ == '__main__':
   app.run(port=app.config['PORT'], debug=app.config['DEBUG'])


















