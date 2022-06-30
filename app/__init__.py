from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_hello_world():
    return 'hello world', 200
