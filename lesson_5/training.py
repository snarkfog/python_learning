# Напишите функцию с названием hello_world, которая будет выводить в консоль фразу - Hello, world!
def hello_world():
    print('Hello, world!')


# Напишите функцию с названием print_square, которая будет принимать параметр num
# и выводить в консоль квадрат числа num.
# Не используйте в теле функции дополнительные переменные
def print_square(num):
    print(float(num ** 2))


# Напишите функцию add_numbers, которая возвращает результат сложения двух своих параметров first и second.
# Дополнительные переменные не использовать. # ... # code # ... result = add_numbers(2, 2) print(result)
def add_numbers(first, second):
    return first + second


result = add_numbers(2, 2)
print(result)


# Найдите и исправьте ошибки в коде:
'''
def table(width=1.5, legs=4, color="brown" ):
    print("Table width -", width)
    print("Table legs -", legs)
    print("Table color -", color)


table()
table(2, color="black", width=2)
table(legs=2)
table(1.2, 2, "gray")
table(1.1, 3)
table(width=2, 4, color="white")
table(color=green, width=2, legs=2)
'''


# Напишите функцию sum_ которая принимает три параметра a, b, c. Параметр “c” равен нулю по умолчанию.
# Функция должна возвращать сумму всех трех аргументов. Не использовать дополнительные переменные.
def sum_(a, b, c=0):
    return a + b + c


# Напишите функцию с именем func которая будет выводить в консоль числа от 0 до 4,
# каждое в новой строке если ее запустить без параметров.
# Либо числа от 0 до n-1, где n – параметр функции.
# Используйте цикл for и переменную итератор i. # ... # code # ... func()
def func(n=5):
    for i in range(n):
        print(i)


func()


# Напишите функцию с именем func которая будет выводить в консоль числа от 0 до 4,
# каждое в новой строке если ее запустить без параметров.
# Либо числа от 0 до n-1, где n – параметр функции.
# Используйте цикл while и переменную итератор i.
# Цикл while должен проверять условие (i != n). # ... # code # ... func()
def func(n=5):
    i = 0
    while i != n:
        print(i)
        i += 1


func()
