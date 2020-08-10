import random, sys

messages = ['It is certain', 'It is decidedly so',
            'Yes, definitely', 'Reply hazy, please try again',
            'Ask again later', 'Concentrate and ask again', 
            'No, probably not', 'Outlook is not so good', 
            'Very doubtful']

while True:
    try:
        print('Please enter your question:')
        input()
        print('My source says: ' + messages[random.randint(0, len(messages) - 1)])
    except KeyboardInterrupt:
        sys.exit()