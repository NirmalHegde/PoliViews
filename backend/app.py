from flask import Flask, jsonify, request
from werkzeug.datastructures import Headers
from PartyClass import Party

app = Flask(__name__)

liberal_party = Party("liberal")
conservative_party = Party("conservative")
ndp_party = Party("ndp")
ppc_party = Party("ppc")
green_party = Party("green")
quebec_party = Party("quebec")

@app.route('/api/search', methods=["GET", "POST"])
def search():

    #required param
    query = request.args['query']

    #optional param
    if len((request.args).keys()) > 1:

        party = request.args['party']
    
    response = {
        "liberal": liberal_party.responseformat,
        "conservative": conservative_party.responseformat,
        "ndp": ndp_party.responseformat,
        "ppc": ppc_party.responseformat,
        "green": green_party.responseformat,
        "quebec": quebec_party.responseformat
    }

    return jsonify(response), 200

# @app.route('/api/search/riding')
# def ridingSearch():

#     postal_code = request.args['postalcode']

#     query = 





if __name__ == "__main__":
    app.run(debug=True)