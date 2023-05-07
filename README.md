# Instructions
0. Install python... obviously
1. Install `requests` if you haven't already (pip install requests or pip3 install requests)
2. Run `python main.py` or `python3 main.py`. Enter in a channel to use, then any additional arguments if needed. It will attempt to download package manifests, then the files with them.

# Channels
latest-client: Downloads the latest Windows client pushed out to regular users

latest-studio64: Downloads the latest Windows Studio x64 version pushed out to regular users

main: Downloads all available clients of a year that were pushed out to regular users
# TODO
Support for multiple channels

Download just the latest packages (still gotta do Mac and other channels)

Sort clients if they are Studio, Studio64 or WindowsPlayer

Make it look less like some sort of debug madness and more user friendly

Clean up and optimize code, it's absolute hell in there and I warn the people who attempt to view it

Support for RCCService (rbxPkgManifest does not exist for RCCService)
