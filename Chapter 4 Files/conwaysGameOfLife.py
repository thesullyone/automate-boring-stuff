# Conway's Game of Life
import random, time, copy

# grid size
width = 60
height = 20
iteration = 1

#create a list of lists for the cells:
nextCells = []
for x in range(width):
    column = [] # create a new column
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # nextCells is a list of column lists
while True: # main loop
    print('\n\n\n\n\n Generation ' + str(iteration) + ": \n") # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    # print currentCells on the screen:
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end ='') # print the # or a space
    # calculate the next step's cells based on current steps'
    for x in range(width):
        for y in range(height):
            # get neightboring coordinates:
            # "% width" ensures leftCoord is always between 0 and width - 1
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            # count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top neighbor alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top right neighbor alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left neighbor alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbor alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom-left neighbor alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbor alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom right neighbor alive
            # set cell based on Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors live
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cell with 3 neighbors animates
                nextCells[x][y] = '#'
            else:
                # everything else dies or stays dead
                nextCells[x][y] = ' '
    iteration +=1
    time.sleep(1) # 1-second pause to prevent flickering
