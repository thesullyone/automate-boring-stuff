catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or hit Enter to stop.)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cats\' names are: ')
for index, name in enumerate(catNames):
    print(str(index + 1) + '. ' + name)