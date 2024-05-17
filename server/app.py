#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route('/count/<parameter>')
def count(parameter):
    result = '0'
    counter = 0
    while counter < int(parameter) - 1:
        result += f"\n{counter + 1}"
        counter += 1
    result += "\n"
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
