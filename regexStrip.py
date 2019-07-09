#! python3
# regexStrip.py - this function does the same thing as the 
# strip() string method. If no other arguments are passed other than
# the string to strip, then whitespace characters will be removed from 
# the beginning and end of the string. Otherwise, the characters specified 
# in the second argument to the function will be stripped.

import re

def stripRegex(string, character):
    if character != '':
        regex = re.compile(character)
        mo = regex.sub('', string)
        print(mo)

    if character == '':
        regex = re.compile(r'^(\s)+|(\s)+$')
        mo = regex.sub('', string)
        print(mo)
    

print('Give me a string you want to strip:')
input1 = str(input())

print('What character(s) should I strip on? (enter nothing for whitespaces at beginning/end of string):')
input2 = str(input())

stripRegex(input1, input2)
