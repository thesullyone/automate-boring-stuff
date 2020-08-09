# program that runs the Collatz sequence on any given
# number until the program returns a 1

def collatz(x):
    if x % 2 == 0:
        print(x // 2)
        return x // 2
    elif x % 2 == 1:
        print(3 * x + 1)
        return 3 * x + 1

while True:
    print("Please enter an integer!")
    try:
        userInput = int(input())
    except ValueError:
        print('Please enter a valid integer!')
    while userInput != 1:
        userInput = collatz(int(userInput))