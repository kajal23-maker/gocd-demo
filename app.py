from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Welcome to Development server!!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
