from flask import Flask
from api.isDev import isDev

app = Flask(__name__)

if __name__ == "__main__":
    app.run('0.0.0.0', port=4000, debug=isDev)