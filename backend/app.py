from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():

    return jsonify({"hello": "world"}), 200

@app.route('/api/search/', methods=["GET"])
def index():

    query = request.args['query']

    return jsonify({"query": query}), 200



if __name__ == "__main__":
    app.run(debug=True)