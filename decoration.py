# Define a decorator function that modifies the behavior of the passed function
def decor(sum):
    # Define an inner function that will modify the value returned by the passed function
    def inner():
        print("Change value of a")  # Print a message
        a = sum  # Assign the value of 'sum' to variable 'a'
        a = a + 5  # Modify 'a' by adding 5
        return a  # Return the modified value of 'a'
    return inner  # Return the inner function

# Define a function that returns a constant value
def sum():
    return 10

# Apply the decorator to the 'sum' function
sum = decor(sum())  # Note: sum() is called here and its return value is passed to decor

# Call the decorated function and print its return value
print(sum())  # Note: 'sum' is now the 'inner' function returned by 'decor'