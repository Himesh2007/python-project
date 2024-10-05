# Define the Calculator class with methods for basic arithmetic operations
class Calculator:
    def __init__(self):
        # Constructor for the Calculator class (not used here but needed for object instantiation)
        pass

    def add(self, x, y):
        # Method to return the sum of x and y
        return x + y

    def subtract(self, x, y):
        # Method to return the difference between x and y
        return x - y

    def multiply(self, x, y):
        # Method to return the product of x and y
        return x * y

    def divide(self, x, y):
        # Method to return the quotient of x divided by y
        if y == 0:
            # Handle division by zero
            return "Cannot divide by zero!"
        return x / y

# Create an instance of the Calculator class
calculator = Calculator()

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
            print(num1, "+", num2, "=", calculator.add(num1, num2))  # Perform addition

        elif choice == '2':
            print(num1, "-", num2, "=", calculator.subtract(num1, num2))  # Perform subtraction

        elif choice == '3':
            print(num1, "*", num2, "=", calculator.multiply(num1, num2))  # Perform multiplication

        elif choice == '4':
            result = calculator.divide(num1, num2)  # Perform division
            print(num1, "/", num2, "=", result)
        
        # Exit the loop after one operation
        break
    else:
        print("Invalid Input")  # Handle invalid menu choice