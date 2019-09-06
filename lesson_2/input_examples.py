string = input("Enter a string: ")
print('You have entered "{}"'.format(string))
print('You have entered "', string, '"', sep='')

print('Press Enter to continue...')
input()

n = int(input('First number: '))
m = int(input('Second number: '))
print('{} + {} = {}'.format(n, m, n + m))
