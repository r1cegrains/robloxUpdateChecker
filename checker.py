import requests
import time

def versionLoop():
    oFile = open("version.txt", "r")
    
    oldVersion = f'{oFile.read()}'
    newVersion = requests.get('') # Grabs the version from Roblox

    if newVersion.text in oldVersion:
        print("no updates")
    else:
        cFile = open("version.txt", "w")
        cFile.write(newVersion.text)
        cFile.close()
        print('Updated version in files')
        print(f'New Roblox version: {newVersion.text}')

while True:
    time.sleep(10) # Loops every 10 seconds
    versionLoop()
