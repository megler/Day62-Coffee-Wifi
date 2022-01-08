# coffeeWifi.py
#
# Python Bootcamp Day 62 - Coffee and Wifi
# Usage:
#      A Flask App that shows a directory of coffee shops with wifi. Day 62 Python Bootcamp
#
# Marceia Egler December 8, 2021

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import csv
import secrets
from forms import CafeForm


SECRET_KEY = secrets.token_urlsafe(16)
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate():
            with open("cafe-data.csv", "a", encoding="utf-8") as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(
                    [
                        form.cafe_name.data,
                        form.cafe_location.data,
                        form.cafe_open.data,
                        form.cafe_close.data,
                        form.coffee_rating.data,
                        form.wifi_strength.data,
                        form.power_avail.data,
                    ]
                )
            return redirect(url_for("add_cafe"))

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
