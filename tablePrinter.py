#! python3
# tablePrinter.py - this program takes a list of lists of strings
# and displays it in a table with each column right-justified
# (Assume that all inner lists contain the same number of strings).

tableData = [['apples', 'oranges', 'cherries', 'banana'],

             ['Alice', 'Bob', 'Carol', 'David'],

             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        colWidths[i] = len((max(table[i], key = len)))
        
    for g in range(len(tableData[0])):
        for i in range(len(table)):
            print(table[i][g].rjust(int(colWidths[i])), end = ' ')
        print('\n')
        
printTable(tableData)
