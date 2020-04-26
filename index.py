from flask import Flask, request
from classes.user import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    user_object = User(request.json)
    return user_object.login()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
