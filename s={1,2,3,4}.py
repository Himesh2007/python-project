# Define two sets
s = {1, 2, 3, 4}  # Set s containing elements 1, 2, 3, and 4
s2 = {4, 5, 6}   # Set s2 containing elements 4, 5, and 6

# Update set s by removing elements that are in set s2
s.difference_update(s2)  # Removes elements from s that are present in s2

# Print the updated set s
print(s)  # Output will be {1, 2, 3}, as 4 was the only common element removed