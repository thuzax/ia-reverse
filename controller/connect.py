from flask import Flask, request
from flask_cors import CORS
from main import main


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return main()

@app.route('/jogar', methods=['POST'])
def jogar():
    return main(request.json)