"""
def add_numbers(first, second):
    return first + second


result = add_numbers(2, add_numbers(5, 7))
print(result)
"""


def add_numbers(first, second):
    print("add_numbers called with", first, second)
    return first + second


add_numbers(9, 10)
result = add_numbers(2, 3) - add_numbers(1, 2)
print(result)
