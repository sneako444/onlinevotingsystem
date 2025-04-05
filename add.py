from flask import Flask

app = Flask(__name__)  # Corrected: use double underscores

@app.route("/")
def home():
    return "Hello from Flask App!"

if __name__ == "__main__":  # Corrected: use double underscores
    app.run(host="0.0.0.0", port=5000)
