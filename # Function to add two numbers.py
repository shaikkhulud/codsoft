
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def calculator():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to exit")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                result = add(num1, num2)
            elif user_input == "subtract":
                result = subtract(num1, num2)
            elif user_input == "multiply":
                result = multiply(num1, num2)
            elif user_input == "divide":
                result = divide(num1, num2)

            print(f"Result: {result}")
        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    calculator()
