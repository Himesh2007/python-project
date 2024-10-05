# Import the regular expression module
import re

# Prompt the user to enter their phone number and store it in 'numbers'
numbers = input("enter your number:-")

# Check if the number matches the Ncell pattern
# Pattern explanation:
# ^981|982|983: The number should start with '981', '982', or '983'
# |: OR
# 971|972|973\d{8}: Or start with '971', '972', or '973' followed by exactly 8 digits
x = re.match(r"^981|982|983|971|972|973\d{8}", numbers)
print(x)  # Print the match object if found, otherwise None

# Check if the match object 'x' is not None and print the result
if x:
    print("the number is Ncell")  # Print this if the number matches the Ncell pattern
else:
    print("the number is invalid")  # Print this if the number does not match the Ncell pattern

# Check if the number matches the NTC pattern
# Pattern explanation:
# ^984|985|986: The number should start with '984', '985', or '986'
# |: OR
# 974|975|976\d{8}: Or start with '974', '975', or '976' followed by exactly 8 digits
z = re.match(r"^984|985|986|974|975|976\d{8}", numbers)
print(z)  # Print the match object if found, otherwise None

# Check if the match object 'z' is not None and print the result
if z:
    print("the number is Ntc")  # Print this if the number matches the NTC pattern
else:
    print("the number is invalid")  # Print this if the number does not match the NTC pattern