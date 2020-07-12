import random
from flask import Flask, render_template
from data import tours, departures, title, subtitle, description

app = Flask(__name__)


@app.route("/")
def index_render():
    list_of_tours = random.sample(list(tours), 6)
    return render_template(
        "index.html",
        tours=tours,
        title=title,
        departures=departures,
        subtitle=subtitle,
        description=description,
        list_of_tours=list_of_tours
    )


@app.route("/departures/<departure>/")
def departures_render(departure):
    tour_on_departure = {}
    for k, v in tours.items():
        if v["departure"] == departure:
            tour_on_departure[k] = v

    tour_price = []
    tour_nights = []
    for v in tour_on_departure.values():
        tour_price.append(v["price"])
        tour_nights.append(v["nights"])
    min_price = min(tour_price)
    max_price = max(tour_price)
    min_nights = min(tour_nights)
    max_nights = max(tour_nights)

    return render_template(
        "departure.html",
        departures=departures,
        departure=departure,
        tour_on_departure=tour_on_departure,
        title=title,
        min_price=min_price,
        max_price=max_price,
        min_nights=min_nights,
        max_nights=max_nights,
    )


@app.route("/tours/<int:id>/")
def tours_render(id):
    return render_template(
        "tour.html", tours=tours, departures=departures, id=id, title=title
    )


if __name__ == "__main__":
    app.run()
