#! python 3

# madLib.py - this program lets users add their own text anywhere the word ADJECTIVE, NOUN, or VERB appears in a string.
# Results are printed to the screen and written to a text file.

import re

# Make new text file with a mad lib sentence.
madLibFile = open('madLibTemplate.txt', 'w')
madLibFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
madLibFile.close()

madLibFile = open('madLibTemplate.txt')
content = madLibFile.read()
madLibFile.close()
print(content)

# ADJECTIVE
adjectiveRegex = re.compile(r'ADJECTIVE')
moSearch = adjectiveRegex.search(content)   
if moSearch != None:
    print('Replace ADJECTIVE with:')
    moSub = adjectiveRegex.sub(input(), content, 1)
    inputFile1 = open('madLib1.txt', 'w')
    inputFile1.write(moSub)
    inputFile1.close()

madLibFile1 = open('madLib1.txt')
content = madLibFile1.read()
madLibFile1.close()

# NOUN
nounRegex = re.compile(r'NOUN')
moSearch = nounRegex.search(content)   
if moSearch != None:
    print('Replace NOUN with:')
    moSub = nounRegex.sub(input(), content, 1)
    inputFile1 = open('madLib1.txt', 'w')
    inputFile1.write(moSub)
    inputFile1.close()

madLibFile1 = open('madLib1.txt')
content = madLibFile1.read()
madLibFile1.close()

# VERB
verbRegex = re.compile(r'VERB')
moSearch = verbRegex.search(content)
if moSearch != None:
    print('Replace VERB with:')
    moSub = verbRegex.sub(input(), content, 1)
    inputFile1 = open('madLib1.txt', 'w')
    inputFile1.write(moSub)
    inputFile1.close()

madLibFile1 = open('madLib1.txt')
content = madLibFile1.read()
madLibFile1.close()

# NOUN(2)
nounRegex = re.compile(r'NOUN')
moSearch = nounRegex.search(content)   
if moSearch != None:
    print('Replace NOUN with:')
    moSub = nounRegex.sub(input(), content, 1)
    inputFile1 = open('madLib1.txt', 'w')
    inputFile1.write(moSub)
    inputFile1.close()

madLibFile1 = open('madLib1.txt')
content = madLibFile1.read()
madLibFile1.close()

# Print results to the screen

inputFile1 = open('madLib1.txt')
content = inputFile1.read()
inputFile1.close()
print(content)
