x = float(input("x = "))

if x > 0:
    y = x ** 0.5
else:
    y = x ** 2

print(y)

name = input("Enter your name: ")

if name == "Max":
    print("You have entered", name)
    print("This is my name too")
else:
    print("Your name differs from mine")
