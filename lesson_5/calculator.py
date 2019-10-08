# Задание 3
# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Cannot be divided by zero")


while True:
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))
    operation = input("Enter an operation or 'exit' to stop the program: ")
    result = None

    if operation == "+":
        result = plus(first_number, second_number)
        print("Result:", result)
    elif operation == "-":
        result = minus(first_number, second_number)
        print("Result:", result)
    elif operation == "*":
        result = multiplication(first_number, second_number)
        print("Result:", result)
    elif operation == "/":
        result = division(first_number, second_number)
        print("Result:", result)
    elif operation == 'exit':
        break
    else:
        print("Unsupported operation")
