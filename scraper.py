from bs4 import BeautifulSoup
import requests
import re


page_link = 'https://bitcoin.stackexchange.com/questions/44420/why-does-base58-wif-format-of-pk-have-5-prefix-the-standpoint-of-mathematics'
WIF_length = 50

# Get the page source
# Returns BeautifulSoup object containing page source rows
def getPageSource(url):
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    results = page_content.body.find_all(string=re.compile('.*{0}.*'.format("")), recursive=True)

    return results


def checkWordIsLongerThan(word, num):
    if len(word) > num:
        return True
    else:
        return False


# Get all words from page source row
# Params: 
#   dataSet - BeautifulSoup object of page source
#   charCount - word lenght, disrecard everything lower that this number
# Returns: list
def getCorrectLengthLines(dataSet, charCount):
    ret = []
    for row in results:
        splittedRow = row.split()
        for col in splittedRow:
            splittedCol = col.split()
            if checkWordIsLongerThan(splittedCol[0], charCount):
                ret.append(splittedCol[0])

    return ret

def getCleanWords(words, charCount):
    cleanWords = []
    for word in words:
        splitted = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', word)
        if checkWordIsLongerThan(splitted[0], charCount):
            cleanWords.append(splitted[0])

    return cleanWords

def checkIfValidKey(word):
    if word[0] == "5":
        print ('Key: ' + word + " is valid!")

def checkAllValidKeys(words):
    for word in words:
        checkIfValidKey(word)

results = getPageSource(page_link)
correctLengthLines = getCorrectLengthLines(results, WIF_length)
cleanWords = getCleanWords(correctLengthLines, WIF_length)

checkAllValidKeys(cleanWords)

#print(cleanWords)