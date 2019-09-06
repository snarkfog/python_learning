import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

d = b ** 2 - 4 * a * c  # discriminant

if d < 0:
    print('This equation has no real solution')
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print('This equation has one solution:', x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('This equation has two solutions:', x1, 'and', x2)
