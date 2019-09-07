# 1
string = input('Enter a string: ')
if string != '':
    print('The string is "{}"'.format(string))

# 2
string = input('Enter a string: ')
if string:
    print('The string is "{}"'.format(string))

# 3
number = int(input('Enter an integer: '))
if number != 0:
    print('The number is non zero')
else:
    print('The number is zero')

# 4
number = int(input('Enter an integer: '))
if number:
    print('The number is non zero')
else:
    print('The number is zero')

if string is not None and string != '':
    pass

if string:
    pass
