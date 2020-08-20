from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

#from .citation import Citation

def fetch_data(url):
    data = {}

    url = url.strip()

    # Get html
    res = requests.get(url)

    # make soup
    soup = BeautifulSoup(res.content, 'html.parser')

    data['url'] = url
    parsed_url = urlparse(url)
    data['domain'] = parsed_url.netloc

    # find info
    data['title'] = get_title(soup)
    data['author'] = get_author(soup)
    data['published'] = get_published_date(soup)
    
    return data



def find_all(searches: list, soup):
    results = []
    for s in searches:
        results += soup.find_all(attrs=s)
    
    for res in results:
        res = res['content'] or res.text
        if res is not None:
            return res
    
    return ''


def get_title(soup):
    return soup.select('title')[0].text


def get_author(soup):
    searches =  [
        {'name': 'author'},
        {'property': 'article:author'},
        {'property': 'author'},
        {'rel': 'author'}
    ]
    
    return find_all(searches, soup)

def get_published_date(soup):
    searches = [
        {'name': 'date'},
        {'property': 'published_time'},
        {'name': 'timestamp'},
        {'class': 'submitted-date'},
        {'class': 'posted-on'},
        {'class': 'timestamp'},
        {'class': 'date'},
    ]
    
    return find_all(searches, soup)