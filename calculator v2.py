num1 = float(input("Enter a number: "))
operation = input("Choose operator (+, -, *, /): ")
num2 = float(input("Enter another number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)