# Prompt the user to enter the first number
num1 = float(input("Enter a number: "))

# Prompt the user to choose an operator
operation = input("Choose operator (+, -, *, /): ")

# Prompt the user to enter the second number
num2 = float(input("Enter another number: "))

# Check the chosen operator and perform the corresponding operation
if operation == '+':
    # Perform addition if the operator is '+'
    print(num1 + num2)
elif operation == '-':
    # Perform subtraction if the operator is '-'
    print(num1 - num2)
elif operation == '*':
    # Perform multiplication if the operator is '*'
    print(num1 * num2)
elif operation == '/':
    # Perform division if the operator is '/'
    # Note: Division by zero is not handled in this code
    print(num1 / num2)
else:
    # Handle invalid operator input
    print("Invalid operator. Please choose one of +, -, *, /.")