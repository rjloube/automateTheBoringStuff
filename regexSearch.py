#! python3

# regexSearch.py - this program opens all .txt files in a folder and searches
# for any line that matches a user-supplied regular expression.
# Results are printed to the screen.

import re, os

# Ask user what folder to look in
print('Please provide file path:')
filePath = str(input())

# Ask user to enter a regular expression to look for
print('Please provide exact word or phrase to search for (caps sensitive):')

userRegex = re.compile(str(input()), re.IGNORECASE)

# Search for any line in .txt files in folder that matches regex and print
# results to the screen

for filename in os.listdir(filePath):
    if filename.endswith('.txt'):
        userFile = open(filePath + '\\' + filename)
        content = userFile.readlines()
        userFile.close()
        for i in content:
            mo = userRegex.search(i)
            if mo != None:
                print(i)
