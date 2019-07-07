#! python3
# commaCode.py - this program defines a function that takes a list value as
# an argument and converts it to a string, with each list item comma seperated.

def commaCode(someList):
    output= ''
    output = output + someList[0]
    for i in range(1, len(someList)):
        output = output + ', ' + someList[i]
    print(output)

userList = []

print('How many items are in your list?')
while True:
    try:
        length = int(input())
        break
    except ValueError:
        print('Please enter integers only.')
        continue

for i in range(length):
    print('Please provide list item ' + str(i + 1) + ':')
    userList.append(input())

commaCode(userList)
