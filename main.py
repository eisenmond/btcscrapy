import requests
from bs4 import BeautifulSoup as bs

def souper(req):
    return bs(req.text, "html.parser")


def searcher(NrOfBlocks):
    url = "https://www.blockchain.com/explorer/blocks/btc/{0}"
    for i in range(NrOfBlocks):
        url = url.format(i)
        soup = souper(requests.get(url))
        print(soup)
