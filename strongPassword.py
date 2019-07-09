#! python3
# strongPassword.py - this program makes sure that the password string it is
# passed is strong (at least eight characters long, contains both uppercase 
# and lowercase characters, and has at least one digit). 

import re

def strongPasswordDetection(password):
    
    lengthRegex = re.compile(r'(\d|\w){8}')
    mo = lengthRegex.search(password)
    if mo == None:
        print('Invalid password - insufficient length')
    
    uppercaseRegex = re.compile(r'[A-Z]')
    mo = uppercaseRegex.search(password)
    if mo == None:
        print('Invalid password - must contain at least one uppercase letter')

    lowercaseRegex = re.compile(r'[a-z]')
    mo = lowercaseRegex.search(password)
    if mo == None:
        print('Invalid password - must contain at least one lowercase letter')

    digitRegex = re.compile('\d')
    mo = digitRegex.search(password)
    if mo == None:
        print('Invalid password - must contain at least one digit')

print('Please create a password:')
password = str(input())
strongPasswordDetection(password)
