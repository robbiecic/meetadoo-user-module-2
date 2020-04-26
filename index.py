from flask import Flask, request, make_response
from classes.user import User
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    user_object = User(request.json['data'])
    result = user_object.login()
    if result['statusCode'] == 200:
        resp = make_response(result['response'])
        cookie = result['cookie']
        resp.set_cookie(cookie['name'],
                        cookie['value'], domain=cookie['domain'], expires=cookie['expires'], secure=cookie['secure'], httponly=cookie['httpOnly'], path=cookie['path'])
        return resp
    return result['response'], 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
