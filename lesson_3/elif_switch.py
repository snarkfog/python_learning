# str
print("""Menu:
1. File
2. View
3. Exit
""")

choice = input("Enter your choice: ")
if choice == "1":
    print("You have entered 'File' menu")
elif choice == "2":
    print("You have entered 'View' menu")
elif choice == "3":
    print("Stopping.")
else:
    print("Incorrect choice")

# int
print("""Menu:
1. File
2. View
3. Exit
""")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("You have entered 'File' menu")
elif choice == 2:
    print("You have entered 'View' menu")
elif choice == 3:
    print("Stopping.")
else:
    print("Incorrect choice")
