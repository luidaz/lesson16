import datetime
from flask import Flask, render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def index():
    title = 'Pagrindinis'
    time = datetime.datetime.now()

    return render_template("index.html", title=title, time=time)

@app.route("/about", methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        title = 'Apie mane'
        time = datetime.datetime.now()

        user_name = request.cookies.get('user_name')

        return render_template("about.html", title=title, time=time, name=user_name)
    elif request.method == 'POST':
        title = 'Issiusta sekmingai'

        contact_name = request.form.get('contact-name')
        contact_email = request.form.get('contact-name')
        contact_message = request.form.get('contact-message')

        response = make_response(
            render_template('success.html', title=title)
        )
        response.set_cookie('user_name', contact_name, contact_email, contact_message)

        return response

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
