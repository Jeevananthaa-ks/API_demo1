from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["user_db"]
users = db["users"]


@app.route("/health")
def healthcheck():
    return {"status": "success"}


# ---------------- SIGNUP API ----------------
@app.route('/signup', methods=['POST','GET'])
def signup():

    data = request.get_json()  

    if not data:
        return jsonify({"message": "No JSON data provided"}), 400

    email = data.get("email")
    password = data.get("password")
    fname = data.get("fname")
    lname = data.get("lname")

    if users.find_one({"email": email}):
        return jsonify({"message": "Email already exists"}), 400

    users.insert_one({
        "email": email,
        "password": password,
        "fname": fname,
        "lname": lname
    })

    return jsonify({
        "message": "User created successfully",
        "email": email
    }), 201


# ---------------- LOGIN API ----------------
@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data:
        return jsonify({"message": "No JSON data provided"}), 400

    email = data.get("email")
    password = data.get("password")

    user = users.find_one({"email": email, "password": password})

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful",
        "fname": user["fname"],
        "email": user["email"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)