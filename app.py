from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    a = float(request.form['a'])
    b = float(request.form['b'])
    return render_template('result.html', operation="Addition", result=a + b)

@app.route('/subtract', methods=['POST'])
def subtract():
    a = float(request.form['a'])
    b = float(request.form['b'])
    return render_template('result.html', operation="Subtract", result=a - b)
@app.route('/multiply', methods=['POST'])
def multiply():
    a = float(request.form['a'])
    b = float(request.form['b'])
    return render_template('result.html', operation="Multiply", result=a * b)

@app.route('/divide', methods=['POST'])
def divide():
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = "Error: Division by zero" if b == 0 else a / b
    return render_template('result.html', operation="Divide", result=result)

@app.route('/Modulus', methods=['POST'])
def modulus():
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = a % b
    return render_template('result.html', operation="Modulus", result=result)

if __name__ == '__main__':
    app.run(debug=True)
