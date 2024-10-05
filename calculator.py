# Define functions for basic arithmetic operations
def add(x, y):
    return x + y  # Return the sum of x and y

def subtract(x, y):
    return x - y  # Return the difference between x and y

def multiply(x, y):
    return x * y  # Return the product of x and y

def divide(x, y):
    return x / y  # Return the quotient of x divided by y

# Display the menu for operation selection
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Get the user's choice of operation
    choice = input("Enter choice (1/2/3/4): ")
    
    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        try:
            # Get user input for the numbers to be operated on
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle invalid number input
            continue
        
        # Perform the operation based on user choice
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")  # Perform addition
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")  # Perform subtraction
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")  # Perform multiplication
        elif choice == '4':
            # Perform division and handle division by zero
            if num2 != 0:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Error! Division by zero is not allowed.")
        
        # Ask if the user wants to perform another calculation
        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break  # Exit the loop if the user doesn't want to continue
    else:
        print("Invalid Input")  # Handle invalid menu choice