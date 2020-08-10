catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or hit Enter to stop.)')
    name = input()
    if name == '': # empty string mean no more aminals
        break
    catNames = catNames + [name]
print('The cats\' names are: ')
for x in range(len(catNames)):
    print(str(x + 1) + '. ' + catNames[x])