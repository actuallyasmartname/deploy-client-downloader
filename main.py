import requests, os, sys
channel = input("What channel would you like to download from? (latest-client, latest-studio64, or main): ")
if channel == "latest-client":
    print("Getting latest version of Roblox...")
    latesthash = requests.get("https://s3.amazonaws.com/setup.roblox.com/version")
    print("Done!")
    print("Grabbing manifest file...")
    if latesthash.status_code == 200:
        manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-rbxPkgManifest.txt")
        if manifest.status_code == 200:
            if not os.path.exists(f"{os.getcwd()}/latest-client/{latesthash.text}"):
                os.makedirs(f"{os.getcwd()}/latest-client/{latesthash.text}")
            if not os.path.exists(f"{os.getcwd()}/latest-client/manifests"):
                os.makedirs(f"{os.getcwd()}/latest-client/manifests")
            with open(f"{os.getcwd()}/latest-client/manifests/{latesthash.text}.txt", 'w') as f:
                f.write(manifest.text)
    print("Done!")
    print(f"Downloading {latesthash.text}...")
    with open(f"{os.getcwd()}/latest-client/manifests/{latesthash.text}.txt") as f:
        newest_items = [ x for x in f.read().splitlines() if "." in x ]
        for g in range(0, len(newest_items)):
            file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-{newest_items[g]}", stream=True)
            if file.status_code == 200:
                with open(f"{os.getcwd()}/latest-client/{latesthash.text}/{newest_items[g]}", 'wb') as f:
                    f.write(file.content)
    print("Done!")
    sys.exit()
elif channel == "latest-studio64":
    print("Getting latest version of Studio x64...")
    latesthash = requests.get("https://s3.amazonaws.com/setup.roblox.com/versionQTStudio")
    print("Done!")
    print("Grabbing manifest file...")
    if latesthash.status_code == 200:
        manifest = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-rbxPkgManifest.txt")
        if manifest.status_code == 200:
            if not os.path.exists(f"{os.getcwd()}/latest-studio64/{latesthash.text}"):
                os.makedirs(f"{os.getcwd()}/latest-studio64/{latesthash.text}")
            if not os.path.exists(f"{os.getcwd()}/latest-studio64/manifests"):
                os.makedirs(f"{os.getcwd()}/latest-studio64/manifests")
            with open(f"{os.getcwd()}/latest-studio64/manifests/{latesthash.text}.txt", 'w') as f:
                f.write(manifest.text)
    print("Done!")
    print(f"Downloading {latesthash.text}...")
    with open(f"{os.getcwd()}/latest-studio64/manifests/{latesthash.text}.txt") as f:
        newest_items = [ x for x in f.read().splitlines() if "." in x ]
        for g in range(0, len(newest_items)):
            file = requests.get(f"https://s3.amazonaws.com/setup.roblox.com/{latesthash.text}-{newest_items[g]}", stream=True)
            if file.status_code == 200:
                with open(f"{os.getcwd()}/latest-studio64/{latesthash.text}/{newest_items[g]}", 'wb') as f:
                    f.write(file.content)
    print("Done!")
    sys.exit()
elif channel == "main":
    year = input("What year of clients would you like to download?: ")
    if int(year) < 2009:
        print("DeployHistory does not exist for years before 2009")
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
else:
    input("Channel is not valid! Press enter to continue...")
            
