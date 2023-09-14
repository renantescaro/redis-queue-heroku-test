import requests


def count_words_at_url(url):
    resp = requests.get(url)
    length = len(resp.text.split())
    print(length)
