a = input("enter a letter or alpha")  # Prompt the user to enter a string
b = a  # Assign the input value to variable b
if (b.isdigit()) == True:  # Check if the input is entirely digits
    print("it is digit")  # If the input is digits, print "it is digit"
else:  # If the input is not entirely digits
    print("it contain letter")  # Print "it contain letter"