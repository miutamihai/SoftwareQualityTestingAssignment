from flask import Flask, render_template, url_for, request
from validation import InputForm
from datetime import datetime
from werkzeug.utils import redirect
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
car_insurance_quote = 0


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('result_page', form=form))
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def result_page():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'


if __name__ == '__main__':
    app.run(debug=True)
