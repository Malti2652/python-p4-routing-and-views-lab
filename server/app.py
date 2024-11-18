#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Prints the parameter to the console
    return parameter  # Return the plain string

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter < 0:
        return 'Please provide a non-negative integer.'
    return '\n'.join(str(num) for num in range(parameter)) + '\n'  # Add final newline



@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # 'div' represents division
        if num2 == 0:
            return 'Division by zero is not allowed.'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation. Supported operations are +, -, *, div, and %.'
    
    return str(result)  # Return only the result as a string


if __name__ == '__main__':
    app.run(port=5555, debug=True)


    
