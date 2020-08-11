# prints out any given list with a comma and space, with an
# "and" before the final item
spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(givenList):
    for x in range(len(givenList)):
        if x == 0: # first item in list
            print(givenList[x] , end = '')
        elif x == len(givenList) - 1: # final item in list
            print(', and ' + givenList[x])
        else: # any other item in list
            print(', ' + givenList[x] , end = '')

comma(spam)