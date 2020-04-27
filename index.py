from flask import Flask, request, make_response
import json
from flask_apispec import FlaskApiSpec, use_kwargs, marshal_with
from classes.user import User
from models.LoginSchema import LoginSchema, LoginResponseSchema
from models.ErrorSchema import ErrorSchema


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
@use_kwargs(LoginSchema)
@marshal_with(LoginResponseSchema, code=200)
@marshal_with(ErrorSchema, code=400)
def login(**kwargs):
    if 'data' in request.json:
        user_object = User(request.json['data'])
        result = user_object.login()
    else:
        return 'Poorly formed body', 400

    if result['statusCode'] == 200:
        resp = make_response(result['response'])
        cookie = result['cookie']
        resp.set_cookie(cookie['name'],
                        cookie['value'], domain=cookie['domain'], expires=cookie['expires'], secure=cookie['secure'], httponly=cookie['httpOnly'], path=cookie['path'])
        return resp
    return result['response'], 400


# Retrieves a given user in path
@app.route('/user/<email_address>', methods=['GET'])
@marshal_with(LoginResponseSchema, code=200)
@marshal_with(ErrorSchema, code=400)
def user_handle(email_address):
    body = {"email": email_address}
    user_object = User(body)
    result = user_object.get_user()
    if result['statusCode'] == 200:
        return result['response'], 200
    return result['response'], 400


# Perform auto-documentation
docs = FlaskApiSpec(app)
docs.register(login)
docs.register(user_handle)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
