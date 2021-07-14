from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import ntc_news

app = Flask(__name__)

@app.route('/')
def home():
    return 'HelloWorld'

@app.route('/api', methods=['GET'])
def get_api():
    return ntc_news.data


if __name__ == "__main__":
    app.run(debug=True)