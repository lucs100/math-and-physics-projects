# Not exactly a math and physics problem, this is a Python solution to the problem posed in this video:
# https://www.youtube.com/watch?v=zp4BMR88260

import re

def loadWords():
    with open('words_alpha.txt') as wordFile:
        validWords = set(wordFile.read().split())

    return validWords

allWords = loadWords()

okWords = {}

checkSets = {
    1: "[gkmqvwxz]",
    2: "[gikmoqvwxz]",
    3: "[gikmoqsvwxz]"
}

mode = 3 # strictness level defined in checkSets

def addToOk(word, length):
    if length in okWords:
        okWords[length].add(word)
    else:
        okWords[length] = {word}

def checkSeg(word):
    if re.search(checkSets[mode], word) == None:
        return True
    return False

for word in allWords:
    length = len(word)
    if length > 8: #arbitrary, help cut down search time
        if checkSeg(word):
            addToOk(word, length)

print(okWords[max(okWords)])
