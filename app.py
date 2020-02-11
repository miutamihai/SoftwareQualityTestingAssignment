from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
car_insurance_quote = 0
premium = 0


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def result_page():
    driver_age = relativedelta(datetime.date(datetime.now()), datetime.strptime(request.form['dateOfBirth'],
                                                                                '%Y-%m-%d')).years
    if driver_age < 18:
        return 'No Quote POSSIBLE'
    global premium
    if request.form['coverType'] == 'Comprehensive':
        premium = 0.04 * int(request.form['vehicleValue'])
    else:
        premium = 0.025 * int(request.form['vehicleValue'])
    if 18 <= driver_age <= 25:
        premium += premium * 0.10
    penalty_points = int(request.form['penaltyPoints'])
    if penalty_points == 0:
        return premium
    elif 1 <= penalty_points <= 4:
        premium += 100
    elif 5 <= penalty_points <= 7:
        premium += 200
    elif 8 <= penalty_points <= 10:
        premium += 300
    elif 11 <= penalty_points <= 12:
        premium += 400
    else:
        return 'No Quote POSSIBLE'
    return render_template('result.html', result=premium)


if __name__ == '__main__':
    app.run(debug=True)
