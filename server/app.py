#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<parameter>")
def count(parameter):
    try:
        num = int(parameter)
        output = ''
        for i in range(num):
            output += str(i) + '\n'
        return output
    except ValueError:
        return 'Invalid parameter. Please provide a valid integer.'

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1 , operation, num2):

    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation."
    
    return str(result)
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
