#Plugin Scraper
import re

import requests
from bs4 import BeautifulSoup

def scrapePlugin(index):
    if index == 1:
        url = 'https://geysermc.org/download/?project=geyser'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for text in soup.find_all('a', href=re.compile("paper")):
            dwnld = text.get('href')
            return dwnld
    elif index == 2:
        url = 'https://papermc.io/downloads/paper'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    elif index == 3:
        url = 'https://www.spigotmc.org/resources/plan-player-analytics.32536/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for text in soup.find_all('a', class_="inner"):
            dwnld = text.get('href')
            return "https://spigotmc.org/" + dwnld
    elif index == 4:
        url = 'https://www.spigotmc.org/resources/chunky.81534/reviews'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for text in soup.find_all('a', class_="inner"):
            dwnld = text.get('href')
            return "https://spigotmc.org/" + dwnld


