# Напишите код в соответствии с инструкциями в задании
"""Создайте переменную A, присвойте ей значение 10.
Выведете сообщение на консоль “A – is greater than 5”, только при условии, если A больше 5."""
A = 10
if A > 5:
    print("A – is greater than 5")

# Напишите код в соответствии с инструкциями в задании
"""Создайте переменную “х” и присвойте ей значение 2 
В зависимости от условия, если “x” больше нуля, присвойте переменной “y” значение “x” в степени 0.5. 
В противном случае “y” будет принимать значение – “x” в степени 2 Вывести на консоль значение переменной “y”"""
x = 2
if x > 0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)

# Найдите и исправьте ошибки в коде
if 0 < x < 7:
    print("Значение x входит в данный диапазон!")
    y = 2 * x - 5
    if y < 0:
        print("Значение y отрицательно!")
    else:
        if y > 0:
            print("Значение y положительно!")
        else:
            print("y = 0")

# Напишите код в соответствии с инструкциями в задании
"""Напишите код который бы в зависимости от выбранного пункта меню сохраненного в переменной choice,
выводил бы на консоль соответственно слова “File”, “View”, “Exit”.
Иначе – “Incorrect choice”
print("Menu: 1. File 2. View 3. Exit")
choice = input("Enter your choice: ") # ... # cod # ... """
print("""Menu: 1. File 2. View 3. Exit""")
choice = input("Enter your choice: ")
if choice == "1":
    print("File")
elif choice == "2":
    print("View")
elif choice == "3":
    print("Exit")
else:
    print("Incorrect choice")

# Напишите код в соответствии с инструкциями в задании
"""Присвойте переменной state_msg значение “Ready” либо “Not ready yet” 
в зависимости от состояния логической переменной is_ready. 
Используйте тернарный оператор. is_ready = False # ... # code # ... print(state_msg) """
is_ready = False
state_msg = "Ready" if is_ready else "Not ready yet"
print(state_msg)

# Найдите и исправьте ошибки в коде
"""
if "str":
    print("True")
elif "":
    print("False")
elif 0j:
    print("False")
elif -1:
    print("True")
elif 0.0:
    print("False")
elif None:
    print("False")
elif 1.25:
    print("True")
elif False:
    print("False")
"""
