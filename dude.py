#HW2

from collections import defaultdict
import sys
import string
from typing import List
totalLength = 3 # the default value
grammarRules = defaultdict(list)
theList = [];
count = 0;

n = len(sys.argv)

# looking through args to get needed info
for arg in range(1, n):
    # this finds the length by finding the arg with -l in it
    if sys.argv[arg][0:2] == "-l":
        # if there actually is a number specified after -l
        if len(sys.argv[arg]) != 2:
            totalLength = sys.argv[arg][2:len(sys.argv[arg])] # will take any numbers after -l 

    # this finds which grammar file to use by searching for the arg that has a '.txt' at the end
    elif sys.argv[arg][len(sys.argv[arg])-4:len(sys.argv[arg])-1]:
        grammarFile = sys.argv[arg]

# the grammar part lolz
for line in open(grammarFile, 'r'):
    rule = line.split()
    production = rule[2:]
    prodString = ''

    # adds a key if the rule doesn't exist yet
    if(rule[0] not in grammarRules.keys()):
        for i in production:
            prodString = prodString + i + " "
        grammarRules[rule[0]].append(prodString)
    else: #adds the production to the key's values
        for i in production:
            prodString = prodString + i + " "
        grammarRules[rule[0]].append(prodString)

startChar = open(grammarFile, 'r').readline().split()[0]
theList.append(startChar)
print("");

while (len(theList) != 0):
    lft, index = "",0 #lft = left most terminal
    sentence = theList.pop().split()

    if len(sentence) > int(totalLength):
        continue

    for word in sentence:
        if word in grammarRules.keys():
            lft = word
            index = sentence.index(word)
            break

    if(lft == ''):
        if len(sentence) == int(totalLength):
            for word in sentence:
                print(word, end = " ")
            count+=1;
            print()
        continue

    for value in grammarRules[word]:
        copy = []

        for word in sentence:
            copy.append(word)
        copy.remove(lft)
        copy.insert(index, value)

        storageString = ''

        for word in copy:
            storageString = storageString + word + " "

        theList.append(storageString)

print("");
print("Total generated strings: {} ".format(count));