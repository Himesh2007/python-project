# Define a function to check if a given string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("Yes, it's a palindrome!")  # Output if the string is a palindrome
else:
    print("No, it's not a palindrome.")  # Output if the string is not a palindrome