from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    return jsonify({"reply": "You said: " + user_msg})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
