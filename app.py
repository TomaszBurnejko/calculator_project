from flask import Flask, request, render_template
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = calculator.calculate(expression)
        except Exception as e:
            result = str(e)
    return render_template('app.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)