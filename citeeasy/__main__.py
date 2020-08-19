from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .fetch import fetch_data


with open('sites.txt') as f:
    lines = f.readlines()

data_list = [{} for _ in lines]
count = 0

for url in lines:
    data_list[count] = fetch_data(url)
    count += 1


print(data_list)