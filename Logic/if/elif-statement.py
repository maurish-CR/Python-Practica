def positive_or_negative(number):
    if number > 0:
        return 'Positive!'
    elif number < 0:
        return 'Negative!'
    else:
        return "It's ZEROOOOO!"

print(positive_or_negative(-1))


def calculator(operation, a, b):
    if operation =="add" or operation == "Add":
        return a + b
    elif operation == "subtract":
        return a-b
    elif  operation == "multiply":
        return a*b
    elif operation == "divide":
        return a/b
    else:
        return "Not a valid operation"

print(calculator("add", 1, 2))