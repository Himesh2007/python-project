# Read input from the user
a = input()

# Check if the input starts with 'displaygarnus("' and ends with '")'
if a.startswith("displaygarnus(\"") and a.endswith("\")"):
    # Extract and print the content between 'displaygarnus("' and '")'
    print(a[15:-2])

# Check if the input starts with 'displaygarnus(' and ends with ')'
elif a.startswith("displaygarnus(") and a.endswith(")"):
    # Evaluate and print the content between 'displaygarnus(' and ')'
    print(eval(a[14:-1]))

# Uncomment the following code if 'displaygarnus' is defined in 'display' module

# from display import displaygarnus
# Check if the input starts with 'displaygarnus("' and ends with '")'
# if a.startswith("displaygarnus(\"") and a.endswith("\")"):
#     # Call the function 'displaygarnus' with the extracted argument
#     displaygarnus(a[15:-2])
# Check if the input starts with 'displaygarnus(' and ends with ')'
# elif a.startswith("displaygarnus(") and a.endswith(")"):
#     # Call the function 'displaygarnus' with the evaluated argument
#     displaygarnus(eval(a[14:-1]))