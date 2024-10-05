# Function to handle user registration
def register():
    # Prompt the user to enter a username
    username = input("Enter a username: ")
    # Prompt the user to enter a password
    password = input("Enter a password: ")
    
    # Open the file 'users.txt' in append mode to add new user credentials
    with open("users.txt", "a") as file:
        # Write the username and password to the file, separated by a comma
        file.write(f"{username},{password}\n")
    
    # Print a message indicating successful registration
    print("Registration successful!")

# Function to handle user login
def login():
    # Prompt the user to enter their username
    username = input("Enter your username: ")
    # Prompt the user to enter their password
    password = input("Enter your password: ")
    
    # Open the file 'users.txt' in read mode to check for credentials
    with open("users.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Strip whitespace and split the line into username and password
            user, pwd = line.strip().split(",")
            # Check if the entered username and password match any in the file
            if user == username and pwd == password:
                # Print a success message and return if credentials match
                print("Login successful!")
                return
    
    # Print an error message if no matching credentials are found
    print("Login failed. Please check your username and password.")

# Main function to display the menu and handle user choices
def main():
    # Loop to keep the menu active until the user chooses to exit
    while True:
        # Display menu options to the user
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")
        
        # Handle the user's choice
        if choice == "1":
            # Call the register function to handle registration
            register()
        elif choice == "2":
            # Call the login function to handle login
            login()
        elif choice == "3":
            # Print a message and exit the loop if the user chooses to exit
            print("Exiting...")
            break
        else:
            # Print an error message if the user's choice is invalid
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function to start the program
    main()