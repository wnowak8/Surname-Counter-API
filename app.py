import pandas as pd
from flask import Flask, jsonify, request



app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    surname = request.json.get("surname")


    return jsonify({"access_token": access_token}), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
