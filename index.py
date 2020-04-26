from flask import Flask, request, make_response
from classes.user import User
import json
# from flask_apispec import use_kwargs, marshal_with
from models.LoginSchema import LoginSchema, LoginResponseSchema
from models.ErrorSchema import ErrorSchema
from flask_apispec import FlaskApiSpec, use_kwargs, marshal_with

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# @marshal_with -> response marshalling behavior
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
        # response = LoginResponseSchema(
        #     firstname=result['response']['firstname'], surname=result['response']['surname'], email=result['response']['email'])
        resp = make_response(result['response'])
        cookie = result['cookie']
        resp.set_cookie(cookie['name'],
                        cookie['value'], domain=cookie['domain'], expires=cookie['expires'], secure=cookie['secure'], httponly=cookie['httpOnly'], path=cookie['path'])
        return resp
    return result['response'], 400


# Perform auto-documentation
docs = FlaskApiSpec(app)
docs.register(login)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
