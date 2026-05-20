#Server Scraper

import requests
from bs4 import BeautifulSoup

def scrapeServerJar():
    url = 'https://papermc.io/downloads/paper'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for text in soup.find_all('a', class_="flex flex-1 flex-row items-center gap-8 py-3 pl-5 svelte-mn8nes"):
        dwnld = text.get('href')

    return dwnld


