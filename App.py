from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to my Flask app!"

@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "message": "This is an API endpoint!",
        "status": "success"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "code": 200
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
