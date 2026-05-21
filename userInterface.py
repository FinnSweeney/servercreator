
def addPlugins():
    plugins = []

    print("Welcome to the server builder")
    print("Here are the options for plugins to download: \n 1: Geyser \n 2: Floodgate \n 3: Plan \n 4: Chunky")
    pluginInput = ""
    while pluginInput != "0":
        pluginInput = input("Please enter the number of the plugin you would like to add, or \"0\" to quit: ")
        plugins.append(pluginInput)

    return plugins

def configureGlobal():
    GCFile = "/config/paper-global.yml"
    print("Time to configure global settings")
    with open(GCFile, 'r') as f:
        setting = f.readline()
        print(setting)
        edit = input("would you like to change this setting? (y/n) ")
        if edit == "y":
            #save file to string, edit string, overwrite file with string???
            newVal = input("what would you like the new value to be? ")

