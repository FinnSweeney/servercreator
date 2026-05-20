
def addPlugins():
    plugins = []

    print("Welcome to the server builder")
    print("Here are the options for plugins to download: \n 1: Geyser \n 2: Floodgate \n 3: Plan \n 4: Chunky")
    pluginInput = ""
    while pluginInput != "0":
        pluginInput = input("Please enter the number of the plugin you would like to add, or \"0\" to quit: ")
        plugins.append(pluginInput)

    return plugins

