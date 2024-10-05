a = 11  # Assign the value 11 to variable a
b = 22  # Assign the value 22 to variable b

x = a  # Store the value of a in variable x
a = b  # Assign the value of b to a (a now holds the value 22)
b = x  # Assign the value stored in x (original value of a) to b (b now holds the value 11)

# Print the final values of a and b
print(f"the value of a = {a}")  # Output: the value of a = 22
print(f"the value of b = {b}")  # Output: the value of b = 11