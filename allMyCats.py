#! python3
# allMyCats.py - this program allows user to submit cat names which are appended
# to a list.

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cats names are:')
for name in catNames:
    print(' ' + name)
