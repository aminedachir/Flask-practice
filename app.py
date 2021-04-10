from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hom():
   return render_template('Welcome.html')

@app.route("/Division")
def dv():
   return render_template('Division.html')

@app.route("/multiplication")
def homes():
   return render_template('multiplication.html')

if __name__ == '__main__':
   app.run(port=1234, debug = True)


















