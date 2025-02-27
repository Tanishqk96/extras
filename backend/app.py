from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
app = Flask(__name__)
CORS(app)
app.secret_key = "sessionkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/project1"
mongo = PyMongo(app)

@app.route('/', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400  # Handle missing JSON
        
        name = data.get("name", "Unknown")
        email = data.get("email", "Unknown")

        print(f"Received Name: {name}, Email: {email}")

        return jsonify({"message": "Form submitted successfully!", "data": {"name": name, "email": email}})
    
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Something went wrong"}), 500 
if __name__ == '__main__':
    app.run(debug=True)
