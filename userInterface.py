
def addPlugins():
    plugins = []

    print("Welcome to the server builder")
    print("Here are the options for plugins to download: \n 1: Geyser \n 2: Floodgate \n 3: Plan \n 4: Chunky")
    pluginInput = ""
    while pluginInput != "0":
        pluginInput = input("Please enter the number of the plugin you would like to add, or \"0\" to quit: ")
        plugins.append(pluginInput)

    return plugins
def configureAuto():
    GCFile = "/config/paper-global.yml"
    globalSettings = {
        "player-max-concurrent-chunk-generates: ":"-1",
        "player-max-concurrent-chunk-loads: ":"-1",
        "player-max-chunk-load-rate: ":"-1",
        "player-max-chunk-send-rate: ": "-1",
        "use-display-name-in-quit-message: ": "true",
        "fix-far-end-terrain-generation: ": "false",
        #update
        "io-threads: ": "4",
        "worker-threads: ": "8"
    }
    worldSettings = {
        "optimize-explosions: ":"true",
        "allow-using-signs-inside-spawn-protection: ": "true",
        "netty-threads": "3"
    }
    serverProperties = {
        "difficulty=":"normal",
        "enforce-whitelist=": "true",
        "server-port=": "43075",
        "spawn-protection=": "0",
        "view-distance=": "32",
        "white-list=": "true",
    }
    for setting, value in globalSettings.items():
        config = open(GCFile, "r")
        nConfig = config.read()
        nConfig = nConfig.replace(setting, value)
        config.close()
        config = open(GCFile, "w")
        config.write(nConfig)
        config.close()

            # save file to string, edit string, overwrite file with string???
    for setting, value in globalSettings.items():
        config = open(GCFile, "r")
        nConfig = config.read()
        nConfig = nConfig.replace(setting, value)
        config.close()
        config = open(GCFile, "w")
        config.write(nConfig)
        config.close()

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
            nSetting = setting.split(":")
            nSetting[1] = newVal
            stitchedSetting = nSetting[0] + ":" + nSetting[1]
            config = open(GCFile, "r")
            nConfig = config.read()
            nConfig = nConfig.replace(setting, stitchedSetting)
            config.close()
            config = open(GCFile, "w")
            config.write(nConfig)
            config.close()


