import re  # Import the regular expression module

# Prompt the user to enter their number and store it in 'numbers'
numbers = input("enter your number:-")

# Use re.match to check if the input number matches the pattern
# Pattern explanation:
# ^98: The number should start with '98'
# |: OR
# 97\d{8}: Or start with '97' followed by exactly 8 digits
x = re.match(r"^98|97\d{8}", numbers)

# Print the match object or None
print(x)

# Check if a match object was found
if x:
    print("the number is verified")  # Print this if the number matches the pattern
else:
    print("the number is invalid")  # Print this if the number does not match the pattern