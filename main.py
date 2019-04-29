import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = 'Pagrindinis'
    time = datetime.datetime.now()
    return render_template("index.html", title=title, time=time)


@app.route("/about")
def about():
    title = 'Apie mane'
    return render_template("about.html", title=title)


@app.route("/portfolio")
def portfolio():
    title = 'Mano portfolio'

    portfolio_items = [
        {'period': '2019 - 2019', 'job': 'NA'},
        {'period': '2018 - 2018', 'job': 'NA'},
        {'period': '2017 - 2017', 'job': 'NA'},
    ]

    return render_template("portfolio.html", title=title, items=portfolio_items)


if __name__ == '__main__':
    app.run()
