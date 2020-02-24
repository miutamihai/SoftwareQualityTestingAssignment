from flask import Flask, render_template, request

from config import Config
from functions.calculate_driver_age import calculate_driver_age
from functions.determine_basic_premium import determine_basic_premium
from functions.handle_penalty_points import handle_penalty_points

app = Flask(__name__)
app.config.from_object(Config)
car_insurance_quote = 0
premium = 0


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def result_page():
    driver_age = calculate_driver_age(request.form['dateOfBirth'])
    if driver_age < 18:
        return render_template('result.html', result='No Quote POSSIBLE')
    global premium
    premium = determine_basic_premium(request.form['coverType']) * int(request.form['vehicleValue'])
    if 18 <= driver_age <= 25:
        premium += premium * 0.10
    penalty_points = int(request.form['penaltyPoints'])
    premium, quote_possible = handle_penalty_points(premium=premium, penalty_points=penalty_points)
    return render_template('result.html', result=(quote_possible is True and premium or 'No Quote POSSIBLE'))


if __name__ == '__main__':
    app.run(debug=True)
