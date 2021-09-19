import requests


def sentiment_analysis(array_of_paragraphs):
    base_url = 'https://htn2021-elections.cognitiveservices.azure.com'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': 'd6756d3adf554c65bbfd506903d326a6'}
    sentiment_analysis_endpoint = '/text/analytics/v3.1/sentiment'

    text_to_analyze = ""

    for paragraph in array_of_paragraphs:
        text_to_analyze = text_to_analyze + " " + paragraph
        text_to_analyze = text_to_analyze.replace('"', '')

    request_body_template = {
        "documents": [
            {
                "language": "en",
                "id": "1",
                f"text": "{text_to_analyze}"
            }
        ]
    }

    request_url = base_url + sentiment_analysis_endpoint

    r = requests.post(request_url, json=request_body_template, headers=headers)

    json_response = r.json()

    return json_response['documents'][0]['sentiment']
