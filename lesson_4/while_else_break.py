attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter your password "
                     "(you have {} attempts left): ".format(attempts_left + 1))
    if password == "98eaxc":
        print("Access granted")
        break
else:
    print("Access denied")
