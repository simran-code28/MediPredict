import sys
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_all

app = Flask(__name__)
CORS(app)

# ----------- STORAGE -----------
user_history = {}
users = {}

# ----------- HOME -----------
@app.route("/")
def home():
    return send_from_directory("frontend", "login.html")   # ✅ FIX

# ----------- LOGIN PAGE -----------
@app.route("/login")
def login_page():
    return send_from_directory("frontend", "login.html")   # ✅ FIX

# ----------- DASHBOARD PAGE -----------
@app.route("/dashboard")
def dashboard():
    return send_from_directory("frontend", "index.html")   # ✅ FIX

# ----------- SIGNUP API -----------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username & password required"}), 400

    if username in users:
        return jsonify({"msg": "User already exists"}), 400

    users[username] = password
    return jsonify({"msg": "Signup successful"})

# ----------- LOGIN API -----------
@app.route("/login-user", methods=["POST"])
def login_user():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"msg": "Login success"})
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

# ----------- PREDICT API -----------
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    username = data.get("username")

    diabetes_data = data.get('diabetes')
    heart_data = data.get('heart')
    pcos_data = data.get('pcos')

    if not diabetes_data or not heart_data or not pcos_data:
        return jsonify({"error": "Missing input data"}), 400

    try:
        result = predict_all(diabetes_data, heart_data, pcos_data)

        # ✅ USER HISTORY SAVE
        if username:
            if username not in user_history:
                user_history[username] = []

            user_history[username].append(result)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------- HISTORY API -----------
@app.route('/history', methods=['POST'])
def get_history():
    data = request.get_json()

    if not data:
        return jsonify([])

    username = data.get("username")

    return jsonify(user_history.get(username, []))

# ----------- CLEAR HISTORY -----------
@app.route('/clear-history', methods=['POST'])
def clear_history():
    data = request.get_json()
    username = data.get("username")

    if username in user_history:
        user_history[username] = []

    return jsonify({"msg": "History cleared"})

# ----------- RUN -----------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)