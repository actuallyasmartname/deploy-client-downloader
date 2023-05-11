"The world would be a better place if Roblox packaged Windows DeployClients like they did with Mac" - Nobody

# Instructions
0. Install python... obviously
1. Install `requests` if you haven't already (pip install requests or pip3 install requests)
2. Run `python main.py` or `python3 main.py`. Enter in a channel to use, then any additional arguments if needed. It will attempt to download package manifests (except for Mac, which are all in one zip), then the files with them.

# Channels
See `channels.txt`
# TODO

Support for all channels except channels where all versions are hidden (ZLive2 basically)

Download just the latest packages (still gotta do Mac and other channels)

~~Sort clients if they are Studio, Studio64, WindowsPlayer, etc.~~ Kinda already done for latest versions.

Make it look less like some sort of debug madness and more user friendly

Clean up and optimize code, it's absolute hell in there and I warn the people who attempt to view it

Fallback/mirror servers when client not found (this will probably never be implemented though)

Download from https://androdome.com/DeployHistory, this one's gonna be a tough one though since there's no manifests and no raw DeployHistory file

File integrity check