from flask import Flask, request, jsonify
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentences = sent_tokenize(text)

    # Simple extractive summary (v0.1)
    summary = " ".join(sentences[:3])

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
