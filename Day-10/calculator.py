def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")