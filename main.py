import requests, os, sys, hashlib
channels = ["latest-client", "latest-studio64", "latest-studio", "latest-zlive2-client", "latest-zlive2-studio", "latest-zlive2-client-mac", "latest-zcanary-studio-mac", "latest-zcanary-client-mac", "latest-zcanary-client", "latest-zcanary1-client-mac", "latest-zcanary1-studio-mac", "live", "zintegration", "zcanary", "live-mac", "zcanary1", "zcanary2", "zcanaryapps"] 
channel = input("What channel would you like to download from? (see channels.txt for a list of these): ")
if channel not in channels:
    print("Channel not found!")
    input("Press enter to continue...")
    sys.exit()
def grab_latestnonchannel(version, folder, clientsettings):
    print(f"Getting version hash for {folder}...")
    if clientsettings == True:
        latesthashr = requests.get(f"https://clientsettings.roblox.com/v2/client-version/{version}")
        latesthashs = latesthashr.status_code
        latesthash = latesthashr.json()['clientVersionUpload']
    else:
        latesthashr = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{version}")
        latesthashs = latesthashr.status_code
        latesthash = latesthashr.text
    print("Done!")
    print("Grabbing manifest file...")
    if latesthashs == 200:
        manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash}-rbxPkgManifest.txt")
        if manifest.status_code == 200:
            if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash}"):
                os.makedirs(f"{os.getcwd()}/{folder}/{latesthash}")
            if not os.path.exists(f"{os.getcwd()}/{folder}/manifests"):
                os.makedirs(f"{os.getcwd()}/{folder}/manifests")
            with open(f"{os.getcwd()}/{folder}/manifests/{latesthash}.txt", 'w') as f:
                f.write(manifest.text)
    print("Done!")
    print(f"Downloading {latesthash}...")
    with open(f'{os.getcwd()}/{folder}/manifests/{latesthash}.txt', 'r+')  as f:
        linesm = f.readlines()
        checksum_lines = [line.rstrip() for line in linesm if len(line.rstrip()) == 32]
    with open(f"{os.getcwd()}/{folder}/manifests/{latesthash}.txt") as f:
        newest_items = [ x for x in f.read().splitlines() if "." in x ]
        newest_items.append("rbxManifest.txt")
        if clientsettings == True:
            newest_items.append("API-Dump.json")
            newest_items.append("Full-API-Dump.json")
        for item in newest_items:
            if os.path.exists(f"{os.getcwd()}/{folder}/{latesthash}/{item}"):
                    md5 = hashlib.md5(open(f'{os.getcwd()}/{folder}/{latesthash}/{item}','rb').read()).hexdigest()
                    if md5 in checksum_lines:
                        continue
            file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash}-{item}", stream=True)
            if file.status_code == 200:
                with open(f"{os.getcwd()}/{folder}/{latesthash}/{item}", 'wb') as f:
                    f.write(file.content)
    print("Done!")
    print("Verifying files...")
    files = os.listdir(f"{os.getcwd()}/{folder}/{latesthash}/")
    files.remove("rbxManifest.txt")
    if clientsettings == True:
            files.remove("API-Dump.json")
            files.remove("Full-API-Dump.json")
    for file in files:
        md5 = hashlib.md5(open(f'{os.getcwd()}/{folder}/{latesthash}/{file}','rb').read()).hexdigest()
        if md5 in checksum_lines:
            continue
        else:
            print(f"File {file} has incorrect checksum, redownloading")
            filereq = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash}-{file}", stream=True)
            if filereq.status_code == 200:
                 with open(f"{os.getcwd()}/{folder}/{latesthash}/{file}", 'wb') as f:
                    f.write(filereq.content)
    print("Done!")
    input("Press enter to continue...")
    sys.exit()
def grab_latestchannel(channel, version, folder, useClientSettings, clientSettingsVersion):
    print(f"Getting latest version hash for {folder}...")
    if useClientSettings == True:
        latesthashr = requests.get(f"https://clientsettings.roblox.com/v2/client-version/{clientSettingsVersion}/channel/{channel}")
        latesthash = latesthashr.json()['clientVersionUpload']
        latesthashs = latesthashr.status_code
    elif useClientSettings == False:
        latesthashr = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{version}")
        latesthash = latesthashr.text
        latesthashs = latesthashr.status_code
    print("Done!")
    print("Grabbing manifest file...")
    if latesthashs == 200:
        manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash}-rbxPkgManifest.txt")
        if manifest.status_code == 200:
            if not os.path.exists(f"{os.getcwd()}/{folder}/{latesthash}"):
                os.makedirs(f"{os.getcwd()}/{folder}/{latesthash}")
            if not os.path.exists(f"{os.getcwd()}/{folder}/manifests"):
                os.makedirs(f"{os.getcwd()}/{folder}/manifests")
            with open(f"{os.getcwd()}/{folder}/manifests/{latesthash}.txt", 'w') as f:
                f.write(manifest.text)
    print("Done!")
    print(f"Downloading {latesthash}...")
    with open(f'{os.getcwd()}/{folder}/manifests/{latesthash}.txt', 'r+')  as f:
        linesm = f.readlines()
        checksum_lines = [line.rstrip() for line in linesm if len(line.rstrip()) == 32]
    with open(f"{os.getcwd()}/{folder}/manifests/{latesthash}.txt") as f:
        newest_items = [ x for x in f.read().splitlines() if "." in x ]
        newest_items.append("rbxManifest.txt")
        if useClientSettings == True:
            newest_items.append("API-Dump.json")
            newest_items.append("Full-API-Dump.json")
        for item in newest_items:
            if os.path.exists(f"{os.getcwd()}/{folder}/{latesthash}/{item}"):
                    md5 = hashlib.md5(open(f'{os.getcwd()}/{folder}/{latesthash}/{item}','rb').read()).hexdigest()
                    if md5 in checksum_lines:
                        continue
            file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash}-{item}", stream=True)
            if file.status_code == 200:
                with open(f"{os.getcwd()}/{folder}/{latesthash}/{item}", 'wb') as f:
                    f.write(file.content)   
    print("Done!")
    print("Verifying files...")
    files = os.listdir(f"{os.getcwd()}/{folder}/{latesthash}/")
    files.remove("rbxManifest.txt")
    if useClientSettings == True:
            files.remove("API-Dump.json")
            files.remove("Full-API-Dump.json")
    for file in files:
        md5 = hashlib.md5(open(f'{os.getcwd()}/{folder}/{latesthash}/{file}','rb').read()).hexdigest()
        if md5 in checksum_lines:
            continue
        else:
            print(f"File {file} has incorrect checksum, redownloading")
            filereq = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{latesthash}-{file}", stream=True)
            if filereq.status_code == 200:
                 with open(f"{os.getcwd()}/{folder}/{latesthash}/{file}", 'wb') as f:
                    f.write(filereq.content)
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
def grabfromdeployhistory(channel, qqmode):
    year = input("What year of clients would you like to download?: ")
    if int(year) < 2009:
        print("DeployHistory does not exist for years before 2009, you can't even download versions before 2019 anyways lol")
        input("Press enter to continue...")
        sys.exit()
    os.remove(f"DeployHistory{channel}{year}.txt") if os.path.exists(f"DeployHistory{channel}{year}.txt") else 0
    print("Downloading DeployHistory...")
    if qqmode == True:
        deployhistory = requests.get(f"https://setup.rbxcdn.qq.com/channel/{channel}/DeployHistory.txt")
    else:
        deployhistory = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/DeployHistory.txt")
    with open("DeployHistory.txt", 'wb') as f:
        f.write(deployhistory.content)
    print("Done!")
    print("Filtering DeployHistory...")
    with open(f"DeployHistory.txt", 'r') as f2:
        for line in f2:
            if line == "\n" or line == "Error!\n" or line == "Done!\n":
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line.replace(line, ''))
                continue
            if year in line.split(' ',5)[4]:
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line.split(' ',2)[2])
            else:
                continue
    os.remove("DeployHistory.txt")
    print("Done!")
    print("Downloading manifests...")
    with open(f"DeployHistory{channel}{year}.txt", 'r') as f:
        for line in f:
            if 'version-hidden' in line:
                continue
            manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{line.split(' ', 1)[0]}-rbxPkgManifest.txt")
            if manifest.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/{channel}/{year}"):
                    os.makedirs(f"{os.getcwd()}/{channel}/{year}")
                if not os.path.exists(f"{os.getcwd()}/{channel}/{year}/manifests"):
                    os.makedirs(f"{os.getcwd()}/{channel}/{year}/manifests")
                with open(f"{os.getcwd()}/{channel}/{year}/manifests/{line.split(' ', 1)[0]}.txt", 'w') as f:
                    f.write(manifest.text)
    if not os.path.exists(f"{os.getcwd()}/{channel}/{year}/manifests"):
        print("Error: No manifests were downloaded, try a different year. (all clients before 2019 have been erased from ROBLOX's servers, sorry!)")
        os.remove(f"DeployHistory{channel}{year}.txt")
        input("Press enter to continue...")
        sys.exit()
    print("Done!")
    print("Downloading files from manifests (this will probably take a long time, please stand by)...")
    manifests = os.listdir(f"{os.getcwd()}/{channel}/{year}/manifests")
    for l in manifests:
        print(f"Downloading {os.path.splitext(l)[0]}...")
        with open(f"{os.getcwd()}/{channel}/{year}/manifests/{l}") as f:
            newest_items = [ x for x in f.read().splitlines() if "." in x ]
            for g in range(0, len(newest_items)):
                file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/channel/{channel}/{os.path.splitext(l)[0]}-{newest_items[g]}", stream=True)
                if file.status_code == 200:
                    if not os.path.exists(f"{os.getcwd()}/{channel}/{year}/{os.path.splitext(l)[0]}"):
                        os.makedirs(f"{os.getcwd()}/{channel}/{year}/{os.path.splitext(l)[0]}")
                    with open(f"{os.getcwd()}/{channel}/{year}/{os.path.splitext(l)[0]}/{newest_items[g]}", 'wb') as f:
                        f.write(file.content)
    os.remove(f"DeployHistory{channel}{year}.txt")
if channel == "latest-client":
    grab_latestnonchannel("version", "latest-client", False)
if channel == "latest-studio64":
    grab_latestnonchannel("versionQTStudio", "latest-studio64", False)
if channel == "latest-studio":
    grab_latestnonchannel("WindowsStudio", "latest-studio", True)
if 'client' in channel and 'mac' not in channel and channel != "latest-client":
    grab_latestchannel(channel.split('-',4)[1], "version", channel, False, "N/A")
if 'studio' in channel and 'mac' not in channel and channel != "latest-studio64":
    grab_latestchannel(channel.split('-',4)[1], "N/A", channel, True, "WindowsStudio")
if 'client' in channel and 'mac' in channel:
    grab_latestchannelmac(channel.split('-',4)[1], channel, "version", "RobloxPlayer.zip")
if 'studio' in channel and 'mac' in channel:
    grab_latestchannelmac(channel.split('-',4)[1], channel, "versionStudio", "RobloxStudioApp.zip")
if channel == "zintegration":
    grabfromdeployhistory(channel, True)
if channel == "live":
    qqmode = False
    year = input("What year of clients would you like to download?: ")
    os.remove(f"DeployHistory{channel}{year}.txt") if os.path.exists(f"DeployHistory{channel}{year}.txt") else 0
    if int(year) < 2009:
        print("DeployHistory does not exist for years before 2009, you can't even download versions before 2019 anyways lol")
        input("Press enter to continue...")
        sys.exit()
    print("Downloading DeployHistory...")
    deployhistory = requests.get("https://s3.amazonaws.com/setup.roblox.com/DeployHistory.txt")
    with open("DeployHistory.txt", 'wb') as f:
        f.write(deployhistory.content)
    print("Done!")
    print("Filtering DeployHistory...")
    with open(f"DeployHistory.txt", 'r') as f2:
        for line in f2:
            if line == "\n" or line == "Error!\n" or line == "Done!\n":
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line.replace(line, ''))
                continue
            if year in line.split(' ',5)[4]:
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line.split(' ',2)[2])
            else:
                continue
    os.remove("DeployHistory.txt")
    print("Done!")
    print("Downloading manifests...")
    with open(f"DeployHistory{channel}{year}.txt", 'r') as f:
        for line in f:
            manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{line.split(' ', 1)[0]}-rbxPkgManifest.txt")
            if manifest.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/live/{year}"):
                    os.makedirs(f"{os.getcwd()}/live/{year}")
                if not os.path.exists(f"{os.getcwd()}/live/{year}/manifests"):
                    os.makedirs(f"{os.getcwd()}/live/{year}/manifests")
                with open(f"{os.getcwd()}/live/{year}/manifests/{line.split(' ', 1)[0]}.txt", 'w') as f:
                    f.write(manifest.text)
    if int(year) == 2019:
        print("Attempting to get extra clients from qq.com...")
        qqmode = True
        with open(f"DeployHistory{channel}{year}.txt", 'r') as f:
            for line in f:
                manifest = requests.get(f"https://setup.rbxcdn.qq.com/{line.split(' ', 1)[0]}-rbxPkgManifest.txt")
                if manifest.status_code == 200 and not os.path.exists(f"{os.getcwd()}/live/{year}/manifests/{line.split(' ', 1)[0]}.txt"):
                    print(f"Found version {line.split(' ', 1)[0]} from qq.com")
                    with open(f"{os.getcwd()}/live/{year}/manifests/{line.split(' ', 1)[0]}.txt", 'w') as f:
                        f.write(manifest.text)
    if not os.path.exists(f"{os.getcwd()}/live/{year}/manifests"):
        os.remove(f"DeployHistory{channel}{year}.txt")
        input("Press enter to continue...")
        sys.exit()
    print("Done!")
    print("Downloading files from manifests (this will probably take a long time, please stand by)...")
    manifests = os.listdir(f"{os.getcwd()}/live/{year}/manifests")
    for item in manifests:
        print(f"Downloading {os.path.splitext(item)[0]}...")
        with open(f"{os.getcwd()}/live/{year}/manifests/{item}") as f:
            items = [ x for x in f.read().splitlines() if "." in x ]
            for g in range(0, len(items)):
                file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{os.path.splitext(item)[0]}-{items[g]}", stream=True)
                if file.status_code == 403:
                    file = requests.get(f"https://setup.rbxcdn.qq.com/{os.path.splitext(item)[0]}-{items[g]}", stream=True)
                    if file.status_code == 200:
                        if not os.path.exists(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}"):
                            os.makedirs(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}")
                        with open(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}/{items[g]}", 'wb') as f:
                            f.write(file.content)
                if file.status_code == 200:
                    if not os.path.exists(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}"):
                        os.makedirs(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}")
                    with open(f"{os.getcwd()}/live/{year}/{os.path.splitext(item)[0]}/{items[g]}", 'wb') as f:
                        f.write(file.content)
    os.remove(f"DeployHistory{channel}{year}.txt")
    print("Done!")
    input("Press enter to continue...")
    sys.exit()
if channel == "live-mac":
    qqmode = False
    year = input("What year of clients would you like to download?: ")
    os.remove(f"DeployHistory{channel}{year}.txt") if os.path.exists(f"DeployHistory{channel}{year}.txt") else 0
    if int(year) < 2009:
        print("DeployHistory does not exist for years before 2009, you can't even download versions before 2019 anyways lol")
        input("Press enter to continue...")
        sys.exit()
    print("Downloading DeployHistory...")
    deployhistory = requests.get("https://s3.amazonaws.com/setup.roblox.com/mac/DeployHistory.txt")
    with open("DeployHistory.txt", 'wb') as f:
        f.write(deployhistory.content)
    print("Done!")
    print("Filtering DeployHistory...")
    with open(f"DeployHistory.txt", 'r') as f2:
        for line in f2:
            if line == "\n" or line == "Error!\n" or line == "Done!\n":
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line.replace(line, ''))
                continue
            if year in line.split(' ',5)[4]:
                with open(f"DeployHistory{channel}{year}.txt", 'a') as f4:
                    f4.write(line)
            else:
                continue
    os.remove("DeployHistory.txt")
    print("Done!")
    print("Downloading clients...")
    with open(f"DeployHistory{channel}{year}.txt") as f:
        for item in f:
            version = item.split(' ', 4)[2]
            print(f"Downloading {version}...")
            if item.split(' ', 3)[1] == "Client":
                file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/mac/{version}-RobloxPlayer.zip", stream=True)
                fname = "RobloxPlayer.zip"
            elif item.split(' ', 3)[1] == "Studio": 
                file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/mac/{version}-RobloxStudioApp.zip", stream=True)
                fname = "RobloxStudioApp.zip"
            if file.status_code == 403:
                print("Version erased from ROBLOX servers")
            if file.status_code == 200:
                if not os.path.exists(f"{os.getcwd()}/live-mac/{year}/{version}"):
                    os.makedirs(f"{os.getcwd()}/live-mac/{year}/{version}")
                with open(f"{os.getcwd()}/live-mac/{year}/{version}/{fname}", 'wb') as f:
                    f.write(file.content)
    os.remove(f"DeployHistory{channel}{year}.txt")
    print("Done!")
    input("Press enter to continue...")
    sys.exit()
if 'latest' not in channel:
    grabfromdeployhistory(channel, False)
