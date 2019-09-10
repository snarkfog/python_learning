for attempts_left in range(3, 0, -1):
    password = input("Enter your password "
                     "(you have {} attempts left): ".format(attempts_left))
    if password == "98eaxc":
        print("Access granted")
        break
else:
    print("Access denied")
