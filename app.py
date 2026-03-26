from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "YOUR_OPENROUTER_API_KEY"

@app.route("/")
def home():
    return "AI Chatbot Running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_msg}]
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
