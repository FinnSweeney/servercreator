import re

import requests
from bs4 import BeautifulSoup

def scrapeServerJar():
    url = 'https://hangar.papermc.io/GeyserMC/Geyser'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    print("_______________________")
    for text in soup.find_all('a'):
        dwnld = text.get('href')
        print(dwnld)



if __name__ == '__main__':
    scrapeServerJar()