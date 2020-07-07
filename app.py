import json
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import testMethods as tm

# app is the name of the object
app = Flask(__name__)

# CORS - Cross-Origin Resource Sharing
# allow CORS for all domains on all routes
CORS(app)


@app.route("/")
def hello():
    return "Hello World from Flask"


@app.route('/books', methods=['GET'])
def all_books():
    books = tm.get_books()
    return jsonify({
        'status': 'success',
        'books': books
    })


if __name__ == '__main__':
    # use the config file to get host and parameters
    with open('config.json') as config_file:
        config = json.load(config_file)

    # debug=True enables interactive debugger will be shown for unhandled exceptions
    # and the server will be reloaded when code changes
    app.run(host=config['host'], port=config['port'], debug=True)
