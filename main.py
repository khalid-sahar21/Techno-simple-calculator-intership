def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

while True:
    # Take user input for operation choice
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if the choice is to exit
    if choice == '5':
        print("Exiting the calculator.")
        break

    # Take user input for operands
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input. Please enter a valid choice.")
