from flask import jsonify

def hello():
    return jsonify({'message': 'Hello, world!'})
