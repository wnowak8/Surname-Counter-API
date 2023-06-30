from flask import Flask, jsonify, request
from utils import get_surname_info


app = Flask(__name__)


@app.route('/')
def welcome():
    return jsonify({'info': 'welcome'}), 200


@app.route("/surname", methods=["POST"])
def login():
    gender = request.json.get("gender")
    surname = request.json.get("surname")
    result = get_surname_info(gender=gender, surname=surname)

    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
