import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Welcome to Development server!!</h1>"


port = int(os.environ.get('FLASK_PORT', 5000))
if __name__ == '__main__':
    app.run(debug=True, port=port)
