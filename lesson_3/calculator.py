import math

print("""Operations:
1. +
2. -
3. *
4. /
5. exp
6. sin
7. cos
8. tan
""")

first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = input("Operation's number: ")

result_1 = None
result_2 = None

if operation == "1":
    result_1 = first_number + second_number
elif operation == "2":
    result_1 = first_number - second_number
elif operation == "3":
    result_1 = first_number * second_number
elif operation == "4":
    result_1 = first_number / second_number
elif operation == "5":
    result_1 = pow(first_number, second_number)
elif operation == "6":
    result_1 = math.sin(first_number)
    result_2 = math.sin(second_number)
elif operation == "7":
    result_1 = math.cos(first_number)
    result_2 = math.cos(second_number)
elif operation == "8":
    result_1 = math.tan(first_number)
    result_2 = math.tan(second_number)
else:
    print("Unsupported operation")

if result_1 is not None:
    print("Result-1: '{}'".format(result_1))

if result_2 is not None:
    print("Result-2: '{}'".format(result_2))
