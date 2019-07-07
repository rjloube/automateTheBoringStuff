#! python3
# magic8Ball.py - this program is a magic 8 ball that will provide an answer
# to a yes or no question.

import random

messages = ['It is certain',
            'It is decidely so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

input('Press Enter to receive your answer from the magic 8 ball.')

print(messages[random.randint(0, len(messages) - 1)])
