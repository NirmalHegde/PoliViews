from flask import Flask, json, jsonify, request, redirect
from PartyClass import Party

app = Flask(__name__)

app.secret_key = "HTNPROJ"

parties = {
    "Liberal": Party("Liberal"),
    "Conservative": Party("Conservative"),
    "NDP": Party("NDP"),
    "PPC": Party("PPC"),
    "Green": Party("Green"),
}

@app.route('/api/search', methods=["GET", "POST"])
def search():

    #required param
    query = request.args['query']

    response = {

        "liberal" : {
            "summary" : "",
            "relatedlinks": {
                "linktoarticle": "",
                "sentiment": ""
            }
        }
    }


    #optional param
    if len((request.args).keys()) > 1:

        party = request.args['party']
    
    return jsonify(response)

# @app.route('/api/search/riding')
# def ridingSearch():

#     postal_code = request.args['postalcode']

#     query = 





if __name__ == "__main__":
    app.run(debug=True)