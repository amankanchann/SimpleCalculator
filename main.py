from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
        }
def calculator():
    should_continue = True
    user_input1 = float(input("What's the first number? "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        chose_symbol = input("Pick an operation: ")
        user_input2 = float(input("What's the second number? "))

        answer = operations[chose_symbol](user_input1,user_input2)
        print(f"{user_input1} {chose_symbol} {user_input2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or 'n' for new calculation\n")

        if choice == 'y':
            user_input1 = answer
        else:
            should_continue = False
            print("\n"*20)
            calculator()
calculator()
