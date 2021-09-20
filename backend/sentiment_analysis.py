import requests


def sentiment_analysis(summary):
    base_url = 'https://htn2021-elections.cognitiveservices.azure.com'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': 'API-KEY'}
    sentiment_analysis_endpoint = '/text/analytics/v3.1/sentiment'

    request_body_template = {
        "documents": [
            {
                "language": "en",
                "id": "1",
                f"text": "{summary}"
            }
        ]
    }

    request_url = base_url + sentiment_analysis_endpoint

    r = requests.post(request_url, json=request_body_template, headers=headers)

    json_response = r.json()

    return json_response['documents'][0]['sentiment']
