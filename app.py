from flask import Flask, render_template
from data import tours, departures

app = Flask(__name__)


@app.route("/")
def index_render():
    return render_template("index.html")


@app.route('/departures/<departure>/')
def departures_render(departure):
    return render_template('departure.html')


@app.route('/tours/<int:id>/')
def tours_render(id):
    return render_template('tour.html', tours_data=tours[id], departures=departures)


if __name__ == "__main__":
    app.run(debug=True)
