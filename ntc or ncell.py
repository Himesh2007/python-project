# Ntc 98456
# Ncell 98123
import re
numbers = input("enter your number:-")
x = re.match(r"^981|982|983|971|972|973\d{8}",numbers)
print(x)
if x:
    print("the number is Ncell")
else:
    print("the number is invalid")
z = re.match(r"^984|985|986|974|975|976\d{8}",numbers)
print(z)
if z:
     print("the number is Ntc")
else:
    print("the number is invalid")