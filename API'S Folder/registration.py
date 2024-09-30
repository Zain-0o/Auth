from flask import Flask, request, jsonify
import re

app = Flask(__name__)

users_db = []

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_username_taken(username):
    return any(user['username'] == username for user in users_db)

def is_email_taken(email):
    return any(user['email'] == email for user in users_db)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not username or not email or not password or not confirm_password:
        return jsonify({"error": "All fields are required"}), 400
    
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email address"}), 400
    
    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400
    
    if len(password) < 6:
        return jsonify({"error": "Password should be at least 6 characters long"}), 400
    
    if is_username_taken(username):
        return jsonify({"error": "Username already taken"}), 400
    
    if is_email_taken(email):
        return jsonify({"error": "Email already registered"}), 400
    
    user = {
        "username": username,
        "email": email,
        "password": password 
    }
    users_db.append(user)
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/')
def home():
    return jsonify(message="Welcome to the Registration API!"), 200

if __name__ == '__main__':
    app.run(debug=True)
