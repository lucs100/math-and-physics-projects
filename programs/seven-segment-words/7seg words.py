# Not exactly a math and physics problem, this is a Python solution to the problem posed in this video:
# https://www.youtube.com/watch?v=zp4BMR88260s

import re

def loadWords():
    with open('programs/seven-segment-words/words_alpha.txt') as wordFile:
        validWords = set(wordFile.read().split())

    return validWords

allWords = loadWords()

okWords = {}

checkSets = {
    1: "[gkmqvwxz]",
    2: "[gikmoqvwxz]",
    3: "[gikmoqsvwxz]",
}

def addToOk(word, length):
    if length in okWords:
        okWords[length].add(word)
    else:
        okWords[length] = {word}

def checkSeg(word, mode):
    if re.search(checkSets[mode], word) == None:
        return True
    return False

def formatWords(wordSet):
    wordSet = wordSet.replace('{', "").replace('}', "").replace('\'', "")
    return wordSet
    

for n in range(1, len(checkSets)+1):
    for word in allWords:
        length = len(word)
        if length > 8: #arbitrary, help cut down search time
            if checkSeg(word, n):
                addToOk(word, length)

    ml = max(okWords)
    valids = formatWords(str(okWords[ml]))
    print(f"Exclusion set: {checkSets[n]}\tMaximum length: {str(ml)}\tValid words of maximum length: {valids}")
    okWords = {}

