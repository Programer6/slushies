import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    url = "https://ai.hackclub.com/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": "Tell me a short funny joke!"}],
        "model": "qwen/qwen3-32b"
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    joke = data["choices"][0]["message"]["content"]

    return render_template("index.html", joke=joke, title="AI Joke Generator")

@app.route('/challenge')
def challenge():
    return render_template('challenge.html', title="Daily Challenge")

@app.route('/history')
def history():
    return render_template('history.html', title="Joke History")

if __name__ == "__main__":
    app.run(debug=True)
