first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter operation: ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("Unsupported operation")
