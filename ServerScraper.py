#Server Scraper

import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://papermc.io/downloads/paper'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    print("________________________________________")
    for text in soup.find_all('a', class_="flex flex-1 flex-row items-center gap-8 py-3 pl-5 svelte-mn8nes"):
        print(text)
        print("next")


if __name__ == '__main__':
    scrape()
