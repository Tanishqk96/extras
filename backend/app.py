from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.secret_key = "sessionkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/project1"
mongo = PyMongo(app)
@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
