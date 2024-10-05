import os  # Import the os module to interact with the operating system

# Function to register a new user
def register():
    username = input("Enter a username: ")  # Prompt user to enter a username
    password = input("Enter a password: ")  # Prompt user to enter a password
    # Open the "users.txt" file in append mode
    with open("users.txt", "a") as file:
        # Write the username and password to the file
        file.write(f"{username},{password}\n")
    print("Registration successful!")  # Confirm registration

# Function to log in an existing user
def login():
    username = input("Enter your username: ")  # Prompt user to enter their username
    password = input("Enter your password: ")  # Prompt user to enter their password
    # Open the "users.txt" file in read mode
    with open("users.txt", "r") as file:
        for line in file:  # Loop through each line in the file
            user, pwd = line.strip().split(",")  # Split the line into username and password
            if user == username and pwd == password:  # Check if credentials match
                print("Login successful!")  # Confirm login
                return  # Exit the function after successful login
    print("Login failed. Please check your username and password.")  # Inform about failed login

# Main function to display the menu and handle user choices
def main():
    while True:  # Loop to repeatedly display the menu
        print("1. Register")  # Option to register a new user
        print("2. Login")  # Option to log in an existing user
        print("3. Exit")  # Option to exit the program
        choice = input("Enter your choice: ")  # Prompt user to enter their choice

        if choice == "1":  # If user chooses to register
            register()  # Call the register function
        elif choice == "2":  # If user chooses to log in
            login()  # Call the login function
        elif choice == "3":  # If user chooses to exit
            print("Exiting...")  # Print exit message
            break  # Exit the loop and end the program
        else:  # If user enters an invalid choice
            print("Invalid choice. Please try again.")  # Inform the user and prompt again

# Check if the script is executed directly
if __name__ == "__main__":
    # Check if "users.txt" file exists, create it if it doesn't
    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as file:
            pass  # Create the file and close it immediately
    main()  # Call the main function to start the program