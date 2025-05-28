from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Magazin de vitamine - C, A, D"

@app.route("/produse")
def produse():
    return jsonify([
        {"nume": "Vitamina C", "pret": 25},
        {"nume": "Vitamina A", "pret": 30},
        {"nume": "Vitamina D", "pret": 20}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)