from flask import Flask, request, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    img = "hello!"
    return img



if __name__ == '__main__':
    app.run(port=5000)
