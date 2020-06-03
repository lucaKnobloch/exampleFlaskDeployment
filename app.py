from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json

# loads the config file
with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)

# enable CORS - Cross-Origin Resource Sharing
CORS(app)


@app.route("/")
def hello():
    return "Hello World from Flask"


BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })



if __name__ == '__main__':
    # use the config file to get host and parameters
    with open('config.json') as config_file:
        config = json.load(config_file)

    # debug=True enables interactive debugger will be shown for unhandled exceptions
    # and the server will be reloaded when code changes
    app.run(host=config['host'],debug=True, port=80)
