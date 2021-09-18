from flask import Flask, jsonify, request

app = Flask(__name__)

# def queryAnalyzer(query):

#     political_info = {
#         "justin treadeau": "liberal",
#         "jagmeet singh": "ndp",
#         "erin o'toole": "conservative",
#     }

#     justin_keywords = ['justin', 'treadeau', 'justin treadeau', 'justintreadeau ']
#     jagmeet_keywords = ['jagmeet', 'singh', 'jagmeet singh', 'jagmeetsingh']
#     _keywords = ['erin', 'toole', "erin o' toole", 'erintoole ']




#     for word in query:

#         if political_info[word] 

@app.route('/api/search/', methods=["GET", "POST"])
def index():

    query = request.args['query'] #what the user searches in the frontend

    #body params
    req_data = request.get_json()
    party = req_data['Party']
    candidate = req_data['Candidate']

    #json output
    response = {
        "query": query,
        "party": party,
        "candidate": candidate
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)