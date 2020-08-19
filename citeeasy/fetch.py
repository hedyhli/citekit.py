from .citation import Citation


def fetch_data(url):
    for url in lines:
        url = url.strip()
    
        # Get html
        res = requests.get(url)
    
        # make soup
        soup = BeautifulSoup(res.content, 'html.parser')

        data[count]['url'] = url
        parsed_url = urlparse(url)
        data[count]['domain'] = parsed_url.netloc

        # find title
        data[count]['title'] = soup.select('title')[0].text
        count += 1



def find(searches: dict):
    pass

def get_title(soup):
    pass