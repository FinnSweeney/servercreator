#Server Scraper
from ServerScraper import scrapeServerJar
from userInterface import addPlugins
from pluginScraper import scrapePlugin
from userInterface import configureGlobal

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
    splitString = jarFile.split("/")
    jarName = splitString[len(splitString) - 1]
    with open(shFileName,'a') as f:
        f.write("/*  #!/bin/bash \n")
        f.write("cd \"$(dirname \"$0\")\"\n")
        f.write("# get server jar \n")
        f.write("wget " + jarFile + "\n")
        f.write("java -jar " + jarName + " &\n")
        f.write("MyPID=$! \n")
        f.write("sleep 4m \n")
        f.write("kill $MyPID \n")
    #navigate to plugins folder
        f.write("cd plugins \n")

    #start downloading plugins
    plugins = addPlugins()
    for i in range(len(plugins) - 1):
        print(scrapePlugin(int(plugins[i])))
        with open(shFileName, 'a') as f:
            f.write("wget " + scrapePlugin(int(plugins[i])) + "\n")
    with open(shFileName,'a') as f:
        f.write("cd .. \n")
        f.write("java -jar "+ jarName + " &\n")
        f.write("MyPID2=$! \n")
        f.write("sleep 4m \n")
        f.write("kill $MyPID2 \n")
        f.write("cd plugins \n")
        f.write("mv Floodgate/key.pem Geyser-Spigot\n")
        f.write("cd ..\n")
        configureGlobal()









