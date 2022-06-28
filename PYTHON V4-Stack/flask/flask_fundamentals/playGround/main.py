from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "go to http://localhost:5000/play to have it do something "

@app.route("/play")
def play():
    return render_template('playground.html')

@app.route("/play/<num>")
def repeat(num):
    return render_template('playground2.html',_num = int(num))


@app.route("/play/<num>/<color>")
def color(num,color):
    return render_template('playground3.html', _num = int(num), _color = color)


if __name__ == "__main__":
    app.run(debug = True)
