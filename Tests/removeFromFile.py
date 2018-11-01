


def removeFromFile(word):
    f = open("links.txt", "r+")
    lines = f.readlines()
    f.seek(0)

    for line in lines:
        if line.rstrip() != word:
            f.write(line)

    f.truncate()
    f.close()


removeFromFile("test3")