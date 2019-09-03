first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = input("Operation: ")

result = None

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    print("Unsupported operation")

if result is not None:
    print(result)
