from flask import Flask, request, render_template, flash, redirect
from forex_python.converter import CurrencyCodes
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

c = CurrencyCodes()
BASE_URL = "http://api.exchangerate.host/"
API_KEY = "e07cb312c118ee2da462e591ee4f6211"

@app.route('/')
def home_page():
    """Loads home page"""
    return render_template('form.html')

@app.route('/result', methods=["post"])
def show_results():
    convert_from = request.form['convert-from'].upper()

    convert_to = request.form['convert-to'].upper()
    convert_to_symbol = c.get_symbol(f'{convert_to}')
    amount = request.form['amount']

    res = requests.get(f'{BASE_URL}/convert?access_key={API_KEY}&from={convert_from}&to={convert_to}&amount={amount}').json()
    check_err = res.get('success')
    if (not check_err):
         err = res.get('error')
         num_err = err.get('type')
         if num_err == 'invalid_from_currency':
             flash('Please enter a valid "from" currency.')
             return redirect("/")
         if (num_err == 'invalid_to_currency'):
             flash('Please enter a valid "to" currency.')
             return redirect("/")
         if (num_err == 'invalid_conversion_amount'):
             flash('Please enter a valid "amount".')
             return redirect("/")
    num = round(res.get('result'), 2)
    final_num = ('{:,}'.format(num))
    return render_template('result.html', num=final_num, sbl=convert_to_symbol)