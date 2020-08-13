# generates 10k resulting sets of 100 coin flips each, then determines the
# probability of landing 6 of the same side in a row 

import random

numberOfStreaks = 0
flipResults = []
streak = 0

for experimentNumber in range(10000):
    for flip in range(100): # creates a list of 100 'heads' or 'tails' values.
        flipResults.append(random.randint(0,1))
        if flipResults[flip] == flipResults[flip - 1]: # 2 in a row increases this by 1
            streak += 1
        elif flipResults[flip] != flipResults[flip - 1]:
            streak = 0
        if streak == 6: # checks if there is a streak of 6 heads or tails in a row.
            numberOfStreaks += 1
            streak = 0
    print(flipResults)
    flipResults = []
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# me did it ))
