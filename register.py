import os  # Import the os module to interact with the operating system

# Prompt user to choose between registration and login
inp = int(input("1. Register 2. Login"))  # Read user input and convert it to an integer

# Check if the user chose to register
if inp == 1:  # Note: Changed to 'if inp == 1' to match integer comparison
    username = input("Enter a username: ")  # Prompt user to enter a username
    password = input("Enter a password: ")  # Prompt user to enter a password
    
    # Check if the "signup" directory exists, create it if it doesn't
    if not os.path.exists("/signup"):  # Check if the directory "/signup" does not exist
        os.mkdir("/signup")  # Create the directory "/signup"
    
    # Open a file for writing in the "/signup" directory with the username as the filename
    with open(f"/signup/{username}.txt", "w") as file:
        file.write(f"{username} {password}")  # Write the username and password to the file
        print("Signup successful!")  # Inform the user that signup was successful
        print("You are registered successfully!")  # Confirm the registration