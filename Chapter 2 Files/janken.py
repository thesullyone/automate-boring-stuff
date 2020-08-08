import random, sys

#stat variables
wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')
while True: # main loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # player input
        print('Enter your move: (r)ock, (p)aper, (s)cissors. Enter q to quit.')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break input loop
    # display what player chose
    if playerMove == 'r':
        print('ROCK vs. ')
    elif playerMove == 'p':
        print('PAPER vs. ')
    elif playerMove == 's':
            print('SCISSORS vs. ')
    #Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    #Display and record the win/loss
    if playerMove == computerMove:
        print('Tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You\'re Winner!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You\'re Winner!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You\'re Winner!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Your looser!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Your looser!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Your looser!')
        losses = losses + 1