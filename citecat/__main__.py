from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .fetch import fetch_data
from .formatter import format_harvard


with open('sites.txt') as f:
    lines = f.readlines()

lines = [i.split()[0] for i in lines]

data_list = [{} for _ in lines]
count = 0

for url in lines:
    data_list[count] = fetch_data(url)
    count += 1

citations = format_harvard(data_list)

with open('out.txt', 'w') as f:
    f.write('\n'.join(citations))