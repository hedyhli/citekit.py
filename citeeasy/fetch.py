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

    # find title
    data['title'] = get_title(soup)
    
    return data



def find(searches: list):
    pass

def get_title(soup):
    return soup.select('title')[0].text