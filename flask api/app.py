from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    return jsonify({'name': 'Test user '})

if __name__ == '__main__':
    app.run(debug=True , port=5001)