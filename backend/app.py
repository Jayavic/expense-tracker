from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "CloudForge Expense Tracker",
        "message": "Backend is running successfully from feature branch",
        "status": "OK"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
