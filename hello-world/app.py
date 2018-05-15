from flask import Flask
import os

HUMAN_USERNAME = os.getenv('HUMAN_USERNAME', 'World')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello " + HUMAN_USERNAME + "! - Nectarians"


if __name__ == '__main__':
    app.run(debug=True)
