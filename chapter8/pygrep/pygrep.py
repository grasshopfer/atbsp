#! python3

# Usage: pygrep.py <directory> <regex>

import sys, os, re

args = sys.argv

if len(args) < 3:
    print('Usage: pygrep.py <directory> <regex>')

userPattern = re.compile(args[2])

fileList = os.listdir(args[1])
os.chdir(args[1])

# get list of files ending in .txt
txtMatch = re.compile(r'[\S]+\.txt')
txtList = []
for file in fileList:
    if txtMatch.match(file):
        txtList.append(file)

for file in txtList:
    thisFile = open(file,'r').read().split('\n')
    for i,line in enumerate(thisFile):
        if userPattern.match(line):
            print(file + ' ' + str(i) + ' ' + line)




results = []
print(results)
