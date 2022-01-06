import requests
import time

def versionLoop():
    oFile = open("", "r") # Opens the file to read
    
    oldVersion = f'{oFile.read()}'
    newVersion = requests.get('') # Grabs the version from Roblox

    if newVersion.text in oldVersion:
        print("no updates")
    else:
        cFile = open("version.txt", "w") # Opens the file to write the new version
        cFile.write(newVersion.text)
        cFile.close() # Closes the file
        print('Updated version in files')
        print(f'New Roblox version: {newVersion.text}')

while True:
    time.sleep(10) # Loops every 10 seconds
    versionLoop()
