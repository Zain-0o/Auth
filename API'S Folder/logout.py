from flask import Flask, session, redirect, url_for, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        session['username'] = username
        return jsonify(message=f'Logged in as {username}', status=200)
    else:
        return jsonify(message="Username not provided", status=400)


@app.route('/logout', methods=['POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return jsonify(message="Logged out successfully", status=200)
    else:
        return jsonify(message="No active session", status=400)


@app.route('/')
def home():
    if 'username' in session:
        return jsonify(message=f"Logged in as {session['username']}")
    return jsonify(message="You are not logged in")


if __name__ == '__main__':
    app.run(debug=True)
