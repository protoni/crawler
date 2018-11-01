# Reads links from links.txt file and passes them to scraper.
# Also deletes the link once the link and all the sublinks have been parsed.

import os

linksFile = os.getcwd() + "/links.txt"

def removeFromFile(word):
    global linksFile
    f = open(linksFile, "r+")
    lines = f.readlines()
    f.seek(0)

    for line in lines:
        if line.rstrip() != word.rstrip():
            
            f.write(line)

    f.truncate()
    f.close()

def getLinks():
    global linksFile

    f = open(linksFile, "r")
    lines = f.readlines()
    f.close()

    if lines:
        removeFromFile(lines[0])
        return lines[0]
    else:
        return False

    