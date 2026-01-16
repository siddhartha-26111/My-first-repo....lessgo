import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def percentage(n1, n2):
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": percentage,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("number very first you pick: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("what operation you want to select?: ")
        next_number = float(input("What is the next number?: "))

        result = operations[operation_symbol](first_number, next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {result}")

        choice = input("Type 'y' to continue, 'n' to start new: ")

        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

