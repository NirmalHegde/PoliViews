from flask import Flask, jsonify, request, session
import requests
from flask_cors import CORS
# from werkzeug.datastructures import Headers
from PartyClass import Party
import fancy_scraper
import summary
from sentiment_analysis import sentiment_analysis

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "HTNPROJ"

liberal_party = Party("liberal")
conservative_party = Party("conservative")
ndp_party = Party("new democratic")
ppc_party = Party("people")
green_party = Party("green")
quebec_party = Party("quebec")


@app.route('/api/search', methods=["GET", "POST"])
def search():

    # required param
    query = request.args['query']
    session['query'] = query

    liberal_party.addSummary(summary.summarizer(
        fancy_scraper.get_liberal_info(query), query))
    conservative_party.addSummary(summary.summarizer(
        fancy_scraper.get_conservative_info(query), query))
    ndp_party.addSummary(summary.summarizer(
        fancy_scraper.get_ndp_info(query), query))
    green_party.addSummary(summary.summarizer(
        fancy_scraper.get_greenparty_info(query), query))
    ppc_party.addSummary(summary.summarizer(
        fancy_scraper.get_peoplesparty_info(query), query))
    quebec_party.addSummary(summary.summarizer(
        fancy_scraper.get_bloc_quebecois_info(query), query))

    response = {
        "liberal": liberal_party.summary,
        "conservative": conservative_party.summary,
        "ndp": ndp_party.summary,
        "ppc": ppc_party.summary,
        "green": green_party.summary,
        "quebec": quebec_party.summary
    }

    return jsonify(response), 200


@app.route('/api/related-articles')
def relatedArticles():

    party = request.args['party']
    query = request.args['query']
    #query = session.get('query')

    articles = fancy_scraper.get_related_articles(query, party)
    
    links = []
    pictures = []
    titles = []
    sentiments = []

    for article in articles:
        links.append(article[0])
        titles.append(article[1])
        pictures.append(article[2])

    for link in links:
        if (len(link.strip())):
            # Link exists:
            # Get summary of article
            s = summary.summarizer_url(link)
            # Get sentiment analysis from summary or article
            sentiment = sentiment_analysis(s)
            # Add sentiment to array
            sentiments.append(sentiment)

    user_party = Party(party)
    user_party.addRelatedLink(links, sentiments, titles, pictures)

    response = {
        party: [
            {},
            {},
            {}
        ]
    }

    i = 0 
    for i in range(3):
        response[party][i]['link'] = links[i]
        response[party][i]['picture'] = pictures[i]
        response[party][i]['title'] = titles[i]
        response[party][i]['sentiment'] = sentiments[i]

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
