#! python3

"""
collatz.py - this program lets a user provide an integer to begin the
# Collatz sequence with. Starting this sequence with any integer will always
lead to 1.
"""

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        print(3 * number + 1)
        return(3 * number + 1)

print('Give me a number: ')
n = int(input())
while n != 1:
    n = collatz(n)
