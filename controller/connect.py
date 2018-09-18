from flask import Flask, request
from main import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    return main()

@app.route('/jogar', methods=['POST'])
def jogar():
    print(request.json)
    return main(request.json)