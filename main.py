import requests, os, sys
channel = input("What channel would you like to download from? (see channels.txt for a list of these): ")
def grab_latestnonchannel(version, folder):
    print(f"Getting version hash for {folder}...")
    latesthash = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{version}")
    print("Done!")
    print("Grabbing manifest file...")
    if latesthash.status_code == 200:
        manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-rbxPkgManifest.txt")
        if manifest.status_code == 200:
            if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash.text}"):
                os.makedirs(f"{os.getcwd()}/{folder}/{latesthash.text}")
            if not os.path.exists(f"{os.getcwd()}/{folder}/manifests"):
                os.makedirs(f"{os.getcwd()}/{folder}/manifests")
            with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.text}.txt", 'w') as f:
                f.write(manifest.text)
    print("Done!")
    print(f"Downloading {latesthash.text}...")
    with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.text}.txt") as f:
        newest_items = [ x for x in f.read().splitlines() if "." in x ]
        for g in range(0, len(newest_items)):
            file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-{newest_items[g]}", stream=True)
            if file.status_code == 200:
                with open(f"{os.getcwd()}/{folder}/{latesthash.text}/{newest_items[g]}", 'wb') as f:
                    f.write(file.content)
    print("Done!")
    input("Press enter to continue...")
    sys.exit()
def grab_latestchannel(channel, version, folder, useClientSettings, clientSettingsVersion):
    print(f"Getting latest version hash for {folder}...")
    if useClientSettings == True:
        latesthash = requests.get(f"https://clientsettings.roblox.com/v2/client-version/{clientSettingsVersion}/channel/{channel}")
        print("Done!")
        print("Grabbing manifest file...")
        if latesthash.status_code == 200:
            manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash.json()['clientVersionUpload']}-rbxPkgManifest.txt")
            if manifest.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash.json()['clientVersionUpload']}"):
                    os.makedirs(f"{os.getcwd()}/{folder}/{latesthash.json()['clientVersionUpload']}")
                if not os.path.exists(f"{os.getcwd()}/{folder}/manifests"):
                    os.makedirs(f"{os.getcwd()}/{folder}/manifests")
                with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.json()['clientVersionUpload']}.txt", 'w') as f:
                    f.write(manifest.text)
        print("Done!")
        print(f"Downloading {latesthash.json()['clientVersionUpload']}...")
        with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.json()['clientVersionUpload']}.txt") as f:
            newest_items = [ x for x in f.read().splitlines() if "." in x ]
            for g in range(0, len(newest_items)):
                file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash.json()['clientVersionUpload']}-{newest_items[g]}", stream=True)
                if file.status_code == 200:
                    with open(f"{os.getcwd()}/{folder}/{latesthash.json()['clientVersionUpload']}/{newest_items[g]}", 'wb') as f:
                        f.write(file.content)
        print("Done!")
        input("Press enter to continue...")
        sys.exit()
    else:
        latesthash = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{version}")
        print("Done!")
        print("Grabbing manifest file...")
        if latesthash.status_code == 200:
            manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash.text}-rbxPkgManifest.txt")
            if manifest.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash.text}"):
                    os.makedirs(f"{os.getcwd()}/{folder}/{latesthash.text}")
                if not os.path.exists(f"{os.getcwd()}/{folder}/manifests"):
                    os.makedirs(f"{os.getcwd()}/{folder}/manifests")
                with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.text}.txt", 'w') as f:
                    f.write(manifest.text)
                print("Done!")
                print(f"Downloading {latesthash.text}...")
                with open(f"{os.getcwd()}/{folder}/manifests/{latesthash.text}.txt") as f:
                    newest_items = [ x for x in f.read().splitlines() if "." in x ]
                    for g in range(0, len(newest_items)):
                        file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash.text}-{newest_items[g]}", stream=True)
                        if file.status_code == 200:
                            with open(f"{os.getcwd()}/{folder}/{latesthash.text}/{newest_items[g]}", 'wb') as f:
                                f.write(file.content)
                print("Done!")
                input("Press enter to continue...")
                sys.exit()
def grab_latestchannelmac(channel, folder, version, type):
    print(f"Getting latest version hash for {folder}...")
    latesthash = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/mac/{version}")
    print("Done!")
    print(f"Downloading {latesthash.text}...")
    if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash.text}"):
        os.makedirs(f"{os.getcwd()}/{folder}/{latesthash.text}")
    file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/mac/{latesthash.text}-{type}", stream=True)
    if file.status_code == 200:
        with open(f"{os.getcwd()}/{folder}/{latesthash.text}/{type}", 'wb') as f:
            f.write(file.content)
    print("Done!")
    input("Press enter to continue...")
    sys.exit()
if channel == "latest-client":
    grab_latestnonchannel("version", "latest-client")
elif channel == "latest-studio64":
    grab_latestnonchannel("versionQTStudio", "latest-studio64")
elif channel == "latest-zlive2":
    grab_latestchannel("zlive2", "version", "latest-zlive2", False, "N/A")
elif channel == "latest-zlive2-studio":
    grab_latestchannel("zlive2", "N/A", "latest-zlive2-studio", True, "WindowsStudio")
elif channel == "latest-zlive2-mac":
    grab_latestchannelmac("zlive2", "latest-zlive2-mac", "version", "RobloxPlayer.zip")
elif channel == "latest-zcanary-studio-mac":
    grab_latestchannelmac("zcanary", "latest-zcanary-studio-mac", "versionStudio", "RobloxStudioApp.zip")
elif channel == "latest-zcanary-mac":
    grab_latestchannelmac("zcanary", "latest-zcanary-mac", "version", "RobloxPlayer.zip")
elif channel == "latest-zcanary":
    grab_latestchannel("zcanary", "version", "latest-zcanary", False, "N/A")
elif channel == "latest-zcanary1-mac":
    grab_latestchannelmac("zcanary1", "latest-zcanary1-mac", "version", "RobloxPlayer.zip")
elif channel == "latest-zcanary1-studio-mac":
    grab_latestchannelmac("zcanary1", "latest-zcanary1-studio-mac", "versionStudio", "RobloxStudioApp.zip")
elif channel == "main":
    year = input("What year of clients would you like to download?: ")
    if int(year) < 2009:
        print("DeployHistory does not exist for years before 2009, you can't even download versions before 2020 anyways lol")
        sys.exit()
    print("Downloading DeployHistory...")
    deployhistory = requests.get("https://s3.amazonaws.com/setup.roblox.com/DeployHistory.txt")
    with open("DeployHistory.txt", 'wb') as f:
        f.write(deployhistory.content)
    print("Done!")
    print("Filtering years...")
    with open("DeployHistory.txt") as f:
        lines = (l for l in f if year in l)
        with open(f"DeployHistory{year}unfiltered.txt", 'w') as f2:
            f2.writelines(lines)
    os.remove("DeployHistory.txt")
    print("Done!")
    print("Filtering hashes...")
    with open(f"DeployHistory{year}unfiltered.txt", 'r') as f2:
        for line in f2:
            if year in line.split(' ',4)[4]:
                with open(f"DeployHistory{year}.txt", 'a') as f4:
                    f4.write(line.split(' ',2)[2])
            else:
                continue
    os.remove(f"DeployHistory{year}unfiltered.txt")
    print("Downloading manifests...")
    with open(f"DeployHistory{year}.txt", 'r') as f:
        for line in f:
            manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{line.split(' ', 1)[0]}-rbxPkgManifest.txt")
            if manifest.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/main/{year}"):
                    os.makedirs(f"{os.getcwd()}/main/{year}")
                if not os.path.exists(f"{os.getcwd()}/main/{year}/manifests"):
                    os.makedirs(f"{os.getcwd()}/main/{year}/manifests")
                with open(f"{os.getcwd()}/main/{year}/manifests/{line.split(' ', 1)[0]}.txt", 'w') as f:
                    f.write(manifest.text)
    print("Done!")
    print("Downloading files from manifests (this will take a long time, please stand by)...")
    if not os.path.exists(f"{os.getcwd()}/main/{year}/manifests"):
        print("Error: No manifests were downloaded, try a different year. (all clients before 2020 have been erased from ROBLOX's servers, sorry!)")
        os.remove(f"DeployHistory{year}.txt")
        input("Press enter to continue...")
    else:
        lists = os.listdir(f"{os.getcwd()}/main/{year}/manifests")
        for i in range(0, len(lists)):
            print(f"Downloading {os.path.splitext(lists[i])[0]}...")
            with open(f"{os.getcwd()}/{year}/manifests/{lists[i]}") as f:
                newest_items = [ x for x in f.read().splitlines() if "." in x ]
                for g in range(0, len(newest_items)):
                    file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{os.path.splitext(lists[i])[0]}-{newest_items[g]}", stream=True)
                    if file.status_code == 200:
                        if not os.path.exists(f"{os.getcwd()}/main/{year}/{os.path.splitext(lists[i])[0]}"):
                            os.makedirs(f"{os.getcwd()}/main/{year}/{os.path.splitext(lists[i])[0]}")
                        with open(f"{os.getcwd()}/main/{year}/{os.path.splitext(lists[i])[0]}/{newest_items[g]}", 'wb') as f:
                            f.write(file.content)
        os.remove(f"DeployHistory{year}.txt")
else:
    input("Channel is not valid! Press enter to continue...")
