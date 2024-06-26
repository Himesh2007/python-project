import re
numbers = input("enter your number:-")
x = re.match(r"^98|97\d{8}",numbers)
print(x)
if x:
    print("the number is verified")
else:
    print("the number is invalid")