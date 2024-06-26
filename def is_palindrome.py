def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1]
input = input("Enter a string: ")
if is_palindrome(input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")