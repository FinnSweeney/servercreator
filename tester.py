import re

import requests
from bs4 import BeautifulSoup

def scrapeServerJar():
    url = 'https://geysermc.org/download/?project=geyser'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for text in soup.find_all('a', href=re.compile("spigot")):
        dwnld = text.get('href')
        print(dwnld)



if __name__ == '__main__':
    scrapeServerJar()