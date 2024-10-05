# Define a function named 'add' that takes two parameters x and y
def add(x, y):
    # Return the sum of x and y
    return x + y

# Call the 'add' function with arguments 2 and 4, and print the result
print(add(2, 4))  # Output will be 6

# Redefine 'add' as a lambda function that takes two parameters x and y and returns their sum
add = lambda x, y: x + y

# Call the new 'add' lambda function with arguments 3 and 4, and print the result
print(add(3, 4))  # Output will be 7