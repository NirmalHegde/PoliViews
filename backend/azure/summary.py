import requests


def summarizer(array_of_paragraphs):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"

    text_to_analyze = ""

    for paragraph in array_of_paragraphs:
        text_to_analyze = text_to_analyze + " " + paragraph
        text_to_analyze = text_to_analyze.replace('"', '')

    request_body = {
        "sentences": "3",
        "txt": f"{text_to_analyze}"
    }

    headers = {
        'accept': "application/json",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
        'x-rapidapi-key': "API-KEY"
    }

    r = requests.get(url, headers=headers, params=request_body)
    json_response = r.json()

    return json_response['summary']
