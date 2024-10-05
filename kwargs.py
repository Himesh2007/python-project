# Define a dictionary 'sub' with subject names as keys and their corresponding marks as values.
sub = {"maths": 21, "science": 22}

# Define a function named 'percentage' that accepts keyword arguments.
def percentage(**kwargs):
    # Initialize a variable 'sum' to 0 to store the total sum of the values.
    sum = 0
    # Iterate over the items in the kwargs dictionary.
    for key, value in kwargs.items():
        # Add each value to the sum.
        sum = sum + value
    # Return the total sum.
    return sum

# Call the 'percentage' function with keyword arguments math=99 and english=79, 
# and store the result in the variable 'sum'.
sum = percentage(math=99, english=79)

# Print the result stored in 'sum'.
print(sum)  # Output will be 178