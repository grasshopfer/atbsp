#! python3

# madLibs.py allows users to play madLibs

# Usage: madLibs.py textFile.txt
import sys, os, re

args = sys.argv
if len(args) < 2:
    print('Usage: ' + args[0] + ' text.txt')
    sys.exit()
infile = open(args[1],'r').read()

# get parts of speech from text file
toReplace = []

rePartsOfSpeech = re.compile(r'(ADJECTIVE|ADVERB|VERB|NOUN)')
posInText = rePartsOfSpeech.findall(infile)

# get words from user
userWords = []
for pos in posInText:
    if pos == 'ADJECTIVE':
        print('Enter an adjective:')
        userWord = input()
    elif pos == 'NOUN':
        print('Enter a noun:')
        userWord = input()
    elif pos == 'ADVERB':
        print('Enter an adverb:')
        userWord = input()
    elif pos == 'VERB':
        print('Enter a verb:')
        userWord = input()

    userWords.append(userWord)

# replace parts of speech in text with user word
wordPairs = dict(zip(posInText, userWords))
print(wordPairs)
for pos in posInText:
    #infile = re.sub(r'[^\w]' + pos, wordPairs[pos], infile)
    userWord = wordPairs[pos]
    infile = re.sub(r'([^\w])'+pos,r'\1'+userWord, infile)

print(infile)
open(args[1]+'.madlibbed','w').write(infile)
