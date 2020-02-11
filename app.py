from flask import Flask, render_template, url_for, request
from dateutil.relativedelta import relativedelta
from validation import InputForm
from datetime import datetime
from werkzeug.utils import redirect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
car_insurance_quote = 0


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def result_page():
    driver_age = relativedelta(datetime.date(datetime.now()), datetime.strptime(request.form['dateOfBirth'],
                                                                                '%Y-%m-%d')).years
    return str(driver_age)


if __name__ == '__main__':
    app.run(debug=True)
