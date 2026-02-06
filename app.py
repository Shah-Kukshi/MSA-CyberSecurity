from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Winter Jams Cybersecurity Demo App"

@app.route("/data", methods=["GET"])
def get_sensitive_data():
    # ❌ VULNERABILITY 1: No authentication check
    return jsonify({
        "users": ["Alice", "Bob", "Charlie"],
        "emails": [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com"
        ],
        "internal_note": "This data should not be public"
    })


if __name__ == "__main__":
    # ❌ VULNERABILITY 2: Debug mode enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
