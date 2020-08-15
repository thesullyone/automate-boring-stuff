birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name (or press Enter to quit): ', end ='')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is ' + name + '\'s birthday.')
    else:
        print('I do not have birthday information for ' + name + '.')
        print('What is their birthday? ', end = '')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')