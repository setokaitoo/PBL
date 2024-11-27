from flask import Flask

app = Flask(__name__)

@app.before_request
def setup():
    print("before_first_request works!")

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)