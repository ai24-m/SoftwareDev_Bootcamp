from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def initial_render():
    return render_template('index.html')

@app.route("/<x>")
def forbox(x):
    return render_template("index3.html", num1=int(x))

@app.route("/<x>/<y>")
def chekBord(x,y):
    return render_template("index2.html", num1=int(x), num2=int(y))

if __name__ == "__main__":
    app.run(debug = True)