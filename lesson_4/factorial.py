n = int(input("Enter a number: "))

factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(factorial)
