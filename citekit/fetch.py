from urllib.parse import urlparse
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from dateparser import parse

# from .citation import Citation


def fetch_data(url):
    data = {}
    url = url.strip()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    data["url"] = url
    parsed_url = urlparse(url)
    data["domain"] = parsed_url.netloc

    data["title"] = get_title(soup).strip()
    data["author"] = get_author(soup).strip()
    data["published"] = get_published_date(soup).strip()

    return data


def parse_data(data):
    dt = parse(data["published"])
    if dt is not None:
        data["published"] = dt.year
    return data


def find_all(searches: list, soup):
    results = []
    for s in searches:
        results += soup.find_all(attrs=s)

    for res in results:
        res = res["content"] if "content" in str(res.keys) else res.text
        if res is not None:
            return res

    return ""


def get_title(soup):
    return soup.select("title")[0].text


def get_author(soup):
    searches = [
        {"name": "author"},
        {"property": "article:author"},
        {"property": "author"},
        {"rel": "author"},
    ]

    return find_all(searches, soup)


def get_published_date(soup):
    searches = [
        {"name": "date"},
        {"property": "published_time"},
        {"name": "timestamp"},
        {"class": "submitted-date"},
        {"class": "posted-on"},
        {"class": "timestamp"},
        {"class": "date"},
    ]

    return find_all(searches, soup)
