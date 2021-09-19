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

    request_body_2 = {
        "sentences": "6",
        "url": "https://www.cbc.ca/news/politics/trudeau-6-billion-health-care-1.6149945"
    }

    headers = {
        'accept': "application/json",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
        'x-rapidapi-key': "6e37838737mshea161d89e531defp15e789jsn3caa01b3d0e6"
    }

    r = requests.get(url, headers=headers, params=request_body_2)
    json_response = r.json()

    print(json_response['summary'])
    return json_response['summary']


def summarizer_urls(article_url):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"

    request_body_2 = {
        "sentences": "6",
        "url": f"https://www.cnn.com/2013/07/27/us/september-11-anniversary-fast-facts/index.html"
    }

    headers = {
        'accept': "application/json",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
        'x-rapidapi-key': "6e37838737mshea161d89e531defp15e789jsn3caa01b3d0e6"
    }

    r = requests.get(url, headers=headers, params=request_body_2)
    json_response = r.json()

    return json_response['summary']
