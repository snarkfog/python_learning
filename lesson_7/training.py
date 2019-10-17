# Создайте список, введите количество его элементов и сами значения, выведите эти значения на
# экран в обратном порядке.
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_some_list = some_list[::-1]
print(new_some_list)

# Создайте список с названием int_list который содержит числа от 0 до 9.
# Создайте список char_list который содержит буквы (a, b, c, d, e).
# Создайте пустой список empty_list.
# Встроенную функцию list() не использовать.
int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
char_list = ['a', 'b', 'c', 'd', 'e']
empty_list = []

# Создайте список list_r содержащий числа (0, 1, 2, 3, 4) с использование встроенной функции list().
# Создайте список list_str, основанный на строке "Simple string"
list_r = list(range(5))
list_str = list("Simple string")

# Создайте список list_str на основе фразы "Hello, world!"
# Далее, последовательно выведите на консоль первый элемент списка, пятый и последний.
list_str = list("Hello, world!")
print(list_str[0])
print(list_str[4])
print(list_str[-1])

# Дан список my_list. Создайте срез этого списка с названием sub_list
# 1) sub_list содержит 3 и 4 элемент списка my_list
# 2) sub_list содержит элементы my_list начиная с первого, через один
# 3) sub_list содержит список my_list в обратном порядке
# 4) sub_list содержит последние три элемента my_list в обратном порядке
# 5) sub_list содержит копию списка my_list my_list = [1, 10, 22, 43, 11, -2, 7] # ... # code # ...
my_list = [1, 10, 22, 43, 11, -2, 7]
sub_list = my_list[2:4]
sub_list = my_list[::2]
sub_list = my_list[::-1]
sub_list = my_list[-1:-4:-1]
sub_list = my_list[:]


# Задайте список my_list который будет содержать числа от 0 до 9.
# Используя функцию list(). Создайте функцию func, которая принимает два параметра list_ и num.
# Если число num входит в список list_, функция должна выводить на консоль фразу "This number is in list"
# в противном случае, фразу - "This number is out of list"
# my_list = list(range(10))


def func(list_, num):
    if num in list_:
        print("This number is in list")
    else:
        print("This number is out of list")


# Создайте переменную my_str, которая будет содержать текст - "This is simple text"
# Напишите проверку вхождения подстроки “imp” в my_str. Если данная подстрока присутствует,
# на консоль выдается фраза - "This text is in string"
my_str = "This is simple text"
if "imp" in my_str:
    print("This text is in string")

# Дан список my_list. Выведите на консоль длину этого списка my_list = [4, 6, 0, 9, 11, 23, 1, 10] # ... # code # ...
my_list = [4, 6, 0, 9, 11, 23, 1, 10]
print(len(my_list))

# Задайте список my_list с элементами от 0 до 9.
# 1) Добавьте 11 элемент равный 100
# 2) Удалите третий элемент списка
# 3) Измените 10й элемент списка на 99
my_list = list(range(10))
my_list.append(100)
del my_list[2]
my_list[9] = 99

# Дан список my_list, необходимо вывести на консоль все элементы этого списка по очереди,
# предварительно умножив их на 2. Задачу решить с помощью цикла for.
# Использовать переменную счётчик i. my_list = [3, 1, 1, 6, 12, 0, 44, -23] # ... # code # ...
my_list = [3, 1, 1, 6, 12, 0, 44, -23]
for i in my_list:
    print(i * 2)

# Программа вычисляет числа Фибоначчи с использованием списка. Найдите и исправьте ошибку.
n = 10

fibs = [1, 1]

for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])

print(fibs)
