import requests


def summarizer(array_of_paragraphs):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
    
    text_to_analyze = ""

    if (len(array_of_paragraphs) == 0):
        
        return "This party does not have a view on this." 

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
        'x-rapidapi-key': "6e37838737mshea161d89e531defp15e789jsn3caa01b3d0e6"
    }

    r = requests.get(url, headers=headers, params=request_body)
    json_response = r.json()

    return json_response['summary']


def summarizer_urls(article_url):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"

    request_body = {
        "sentences": "6",
        "url": f"{article_url}"
    }

    headers = {
        'accept': "application/json",
        'x-rapidapi-host': "meaningcloud-summarization-v1.p.rapidapi.com",
        'x-rapidapi-key': "6e37838737mshea161d89e531defp15e789jsn3caa01b3d0e6"
    }

    r = requests.get(url, headers=headers, params=request_body)
    json_response = r.json()

    return json_response['summary']
