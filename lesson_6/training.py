

# Напишите функцию с названием function и параметрами a и b, которая возвращает сумму этих параметров.
# Напишите документационную строку к функции содержащую текст - This function adds two arguments.
def function(a, b):
    """This function adds two arguments"""
    return a + b


# Вывести содержание документационной строки функции the_func() на консоль.
# print(the_func.__doc__)


# Напишите функцию с именем func, которая принимает три параметра a, b, c,
# значения по умолчанию которых 4, 10, -1 соответственно.
# Функция выводит в консоль максимальное значение, минимальное значение, и модуль параметра “c”.
# Для решения задачи используйте встроенные функции Python. Порядок следования переменных не изменять.
def func(a=4, b=10, c=-1):
    print(max(a, b, c))
    print(min(a, b, c))
    print(abs(c))


# Напишите функцию с названием str_revers, которая принимает параметр str_ строку,
# и выводит в консоль перевернутую строку, все символы которой идут в обратном порядке.
# Используйте цикл for, переменную итератор i
def str_revers(str_):
    for i in reversed(str_):
        print(i, end='')


# Напишите функцию с названием function, которая присваивает глобальной переменной var
# значение "new variable" var = "variable" # ... # code # ... function() print(var)
var = "variable"


def function():
    global var
    var = "new variable"


function()
print(var)


# Создайте функцию с именем function(), без параметров.
# Объявите в ней переменную var и присвойте ей значение “variable”.
# Создайте встроенную функцию inner() тоже без параметров,
# которая меняет значение ранее созданной переменной var на новое “new variable”
def function():
    var = "variable"

    def inner():
        nonlocal var
        var = "new variable"


# Напишите функцию с сигнатурой factorial(n) которая возвращает факториал числа n.
# Используйте рекурсию.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Программа рекурсивно вычисляет числа Фибоначчи и выводит 10 из них в консоль.
# Найдите ошибки в коде:
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 11):
    print(fib(i))
