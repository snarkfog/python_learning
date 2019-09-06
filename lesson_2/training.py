# Напишите код в соответствии с инструкциями в задании
# Выведите на печать фразу – Hello, world!
print('Hello, world!')

# Напишите код в соответствии с инструкциями в задании
'''Присвойте переменной number1, значение – 123. 
Переменной number2, значение - 7.8. Переменной str_, значение – «string»'''
number1 = 123
number2 = 7.8
str_ = 'string'

# Напишите код в соответствии с инструкциями в задании
''' Присвойте переменной res1 значение 15 в двоичной системе счисления,
а переменной res2, значение 15 в шестнадцатеричной системе счисления.'''
res1 = 0b1111
res2 = 0xF

'''Найдите и исправьте ошибку в коде, при условии, 
что значения присваиваемые переменным A и B менять нельзя. sum_ = 115'''
A = '15'
B = 100
sum_ = int(A) + B
print(sum_)

# Напишите код в соответствии с инструкциями в задании
'''Создайте логическую переменную bool1 и присвойте ей значение – Истина,
и логическую переменную bool2 со значением - Ложь'''
bool1 = True
bool2 = False

# Напишите код в соответствии с инструкциями в задании
'''Дано: number1 = 500 Создайте переменную number2 и присвойте ей значение переменной number1 в вещественном виде.
Создайте переменную number3 и присвойте ей число 10000.0 в экспоненциальной сокращенной записи.'''
# number1 = 500
# number2 = float(number1)
# number3 = 1e4

# Найти и исправить ошибки в коде
comp1 = 3 + 4j
comp2 = complex(2, 3)
comp3 = complex("6-2j")

# Напишите код в соответствии с инструкциями в задании
'''Даны две переменные:
n1 = 47
n2 = 4
Создайте переменную с именем res1 и присвойте ей результат целочисленного деления n1 на n2.
Создайте переменную с именем res2 и присвойте ей остаток от деления n1 на n2'''
# n1 = 47
# n2 = 4
# res1 = n1 // n2
# res2 = n1 % n2

# Напишите код в соответствии с инструкциями в задании
'''Создайте переменную x и присвойте ей значение - -234.636
Создайте переменную n1 в которой будет находится модуль числа x.
Создайте переменную n2 в которой будет находится результат округления n1 с точностью до 2 знаков после запятой.
Создайте переменную n3 в которую поместите переменную n2 преобразованную к целому типу.
Создайте переменную n4 в которую будет помещен результат возведения n3 в квадрат. Используйте встроенные функции.'''
x = -234.636
n1 = abs(x)
n2 = round(n1, 2)
n3 = int(n2)
n4 = pow(n3, 2)

# Напишите код в соответствии с инструкциями в задании
'''Считаем, что библиотека math подключена.
Создайте переменную PI и присвойте ей значение константы Pi из библиотеки math.
Создайте переменную x и присвойте ей значение PI без дробной части, использую функцию библиотеки math.
Создайте переменную y и присвойте ей значения синуса угла x, используя функцию библиотеки math.'''
import math

PI = math.pi
x = math.trunc(PI)
y = math.sin(x)

# Найти и исправить ошибки в коде
a = 10
b = 2
if a == b:
    print("a = b")
elif a <= b:
    print("a <= b")
elif a > b:
    print("a > b")

# Напишите код в соответствии с инструкциями в задании
'''Создайте переменную str1 и присвойте ей значение - First line of text
Создайте переменную str2 и присвойте ей значение - Second line of text 
Сложите строки с пробелом между ними, присвойте результат переменной string и выведите ее на печать'''
str1 = 'First line of text'
str2 = 'Second line of text'
string = str1 + ' ' + str2
print(string)

# Найти и исправить ошибки в коде
string = """Lorem {} ipsum dolor sit amet,
consectetur
adipiscing
elit, {}
do
eiusmod
tempor
incididunt
ut
labore
et
dolore
magna
aliqua.
"""

print(string.format(1, "send"))

# Программа выводит сумму чисел. Найти и исправить ошибки в коде.
n = int(input("First number: "))
m = int(input("Second number: "))
print("{} + {} = {}".format(n, m, n + m))
