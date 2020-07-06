#!flask/bin/python
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/transfer/<string:country>', methods=['GET'])
def get_tasks(country):
    return jsonify({'alibaba will do:': country})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=True)

