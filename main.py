#Server Scraper
from ServerScraper import scrapeServerJar

def fileCreator():
    temp = scrapeServerJar()
    x = temp.find("paper-")
    y = len(temp)
    nameFile = temp[x:y-4] + ".txt"
    text = open(nameFile,'x')
    return nameFile

if __name__ == '__main__':
    jarFile = scrapeServerJar()
    shFileName = fileCreator()
    with open(shFileName,'a') as f:
        f.write("/*  #!/bin/bash \n")
        f.write("wget " + jarFile + "\n")
        



