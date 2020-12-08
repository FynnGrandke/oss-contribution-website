import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def getGithubSearchResult():
    # FIXME: @FynnGrandke URL needs to be adjustable
    url = 'https://github.com/search?l=TypeScript&p=2&q=label%3Ahelp-wanted&type=Issues'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.findAll('div', {'class': 'f4 text-normal'}):
        print('Something ' + str(tag.find('a').string))
        # for something in tag.find('div', {'class': 'text-normal'}):
        #     print('Meetup: ' + something)
