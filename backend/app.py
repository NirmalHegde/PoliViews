from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.datastructures import Headers
from PartyClass import Party
import fancy_scraper 
import summary
import sentiment_analysis

app = Flask(__name__)
cors = CORS(app)

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
    

    liberal_party.addSummary(summary.summarizer(fancy_scraper.get_liberal_info(query)))
    conservative_party.addSummary(summary.summarizer(fancy_scraper.get_conservative_info(query)))
    ndp_party.addSummary(summary.summarizer(fancy_scraper.get_ndp_info(query)))
    green_party.addSummary(summary.summarizer(fancy_scraper.get_greenparty_info(query)))
    ppc_party.addSummary(summary.summarizer(fancy_scraper.get_peoplesparty_info(query)))
    #quebec_party.addSummary(summary.summarizer(fancy_scraper.get_bloc_quebecois_info(query)))

    response = {
        "liberal": liberal_party.formatResponse(),
        "conservative": conservative_party.formatResponse(),
        "ndp": ndp_party.formatResponse(),
        "ppc": ppc_party.formatResponse(),
        "green": green_party.formatResponse(),
        #"quebec": quebec_party.formatResponse()
    }

    return jsonify(response), 200

# @app.route('/api/search/riding')
# def ridingSearch():

#     postal_code = request.args['postalcode']

#     query = 


if __name__ == "__main__":
    app.run(debug=True)