from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_random_number():
    return jsonify({"random_number": random.randint(1, 100)})
