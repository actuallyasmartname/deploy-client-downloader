"The world would be a better place if Roblox packaged Windows DeployClients like they did with Mac" - Nobody

# DeployClients? Huh?
DeployClients are the clients Roblox uses to push out new updates (which actually used to include RCCService but that's a story for another time). These were introduced during August 2008 and were a step up from the previous CAB file installation process. Practically all version numbers, client types, etc. of DeployClients that were pushed to regular users were added to a file called DeployHistory and have been untouched (apart from a wipe in 2009) for a decade. But, that's for DeployHistory. That's fine and all but what about the actual clients? They were made private in February 2020. Every single damn version before that was public, went unaccessible. People had so much Roblox lost media to find, and then a whole pile got added on top of it.

Although clients from 3 months before this change were restored and API Dumps for older Studio versions were later made public, no plans to reintroduce these clients officially to the public have been made.

FYI: This tool wasn't exactly made to preserve this lost media (although I will probably add another file that cycles through all channels and downloads all clients) but as a little gimmicky project, if you could call it that.

# Instructions
0. Install python... obviously
1. Install `requests` if you haven't already (pip install requests or pip3 install requests)
2. Run `python main.py` or `python3 main.py`. Enter in a channel to use, then any additional arguments if needed. It will attempt to download package manifests (except for Mac, which are all in one zip), then the files with them.

# Channels
See `channels.txt`
# TODO

**PRIORITY: SWITCH TO ASYNCHRONOUS CODE**

Support for all channels except channels where all versions are hidden (ZLive2 basically)

Download just the latest packages (still gotta do Mac and other channels)

Make it look less like some sort of debug madness and more user friendly

Clean up and optimize code, it's absolute hell in there and I warn the people who attempt to view it

Fallback/mirror servers when client not found (this will probably never be implemented though)

Download from https://androdome.com/DeployHistory, this one's gonna be a tough one though since there's no manifests and no raw DeployHistory file
