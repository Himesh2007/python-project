# Define a function named `max` to find the maximum value in a list
def max(list):
    # Initialize the variable `max` with the first element of the list
    max = list[0]
    # Iterate through each element `x` in the list
    for x in list:
        # If the current element `x` is greater than `max`, update `max` with `x`
        if x > max:
            max = x
    # Return the largest element found in the list
    return max

# Initialize a list `l` with integer values
l = [20, 30, 40, 50, 15, 10]

# Print the largest element in the list by calling the `max` function
print("Largest element is:", max(l))