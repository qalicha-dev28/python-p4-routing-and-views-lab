from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # print to console
    return param  # return in browser


# Count route
@app.route('/count/<int:param>')
def count(param):
    # Join numbers with newlines and add a trailing newline
    return '\n'.join([str(i) for i in range(param)]) + '\n'


# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
