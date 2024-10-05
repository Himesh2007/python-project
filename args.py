# Function to calculate the sum of variable number of arguments
def abc(*args):
    sum = 0  # Initialize sum to 0
    for num in args:  # Iterate over each number in the variable arguments
        sum += num  # Add each number to the sum
    return sum  # Return the final sum

# Call the abc function with multiple arguments and print the result
sum = abc(2, 3, 4, 5, 6, 7)
print(sum)  # Output: 27

# Call the abc function with fewer arguments and print the result
sum = abc(3, 4, 5)
print(sum)  # Output: 12