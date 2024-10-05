# Initialize a list `a` with some integer values
a = [1, 4, 5, 5, 4, 6]

# Iterate through each element `i` in the list `a`
for i in a:
    # Check if the current element `i` is equal to 5
    if i == 5:
        # Remove the first occurrence of 5 from the list `a` and print the result
        print(a.remove(5))