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

if __name__ == '__main__':
    app.run(debug=True)
