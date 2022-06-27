from flask import Flask, request, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return "123"

@app.route('/123', methods=['GET', 'POST'])
def login():
    return "123"

if __name__ == '__main__':
    app.run(port=5000)
