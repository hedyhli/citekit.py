from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

with open('sites.txt') as f:
    lines = f.readlines()

data = [{} for _ in lines]
count = 0


print(data)