from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

users = {
    "john": "password123",
    "alice": "mypassword"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"status": "error", "message": "Username and password are required!"}), 400

    if username in users and users[username] == password:
        return jsonify({"status": "success", "message": f"Welcome, {username}!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
