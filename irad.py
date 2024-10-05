import os  # Import the os module to perform operating system dependent functionality

# Define a function to create a file with user-specified content
def create_file():
    # Prompt the user to enter the name of the file to create
    filename = input("Enter the name of the file you want to create (with extension): ")
    # Prompt the user to enter the content to insert into the file
    content = input("Enter the content to insert inside the file: ")
    # Open the file in write mode ('w') which creates the file if it doesn't exist
    with open(filename, 'w') as file:
        # Write the user-provided content to the file
        file.write(content)
    # Inform the user that the file has been created and content inserted
    print(f"File '{filename}' created and content inserted.")

# Define a function to read the content of a file
def read_file():
    # Prompt the user to enter the name of the file to read
    filename = input("Enter the name of the file you want to read (with extension): ")
    # Check if the file exists using os.path.exists
    if os.path.exists(filename):
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Print the file content
            print("File content:")
            print(content)
    else:
        # Inform the user if the file does not exist
        print(f"File '{filename}' does not exist.")

# Define a function to add content to an existing file
def add_content():
    # Prompt the user to enter the name of the file to add content to
    filename = input("Enter the name of the file you want to add content to (with extension): ")
    # Prompt the user to enter the new content to add
    additional_content = input("Enter the new content to add: ")
    # Check if the file exists
    if os.path.exists(filename):
        # Open the file in append mode ('a') which adds content to the end of the file
        with open(filename, 'a') as file:
            # Write the new content, starting on a new line
            file.write("\n" + additional_content)
        # Inform the user that the new content has been added
        print(f"New content added to '{filename}'.")
    else:
        # Inform the user if the file does not exist
        print(f"File '{filename}' does not exist.")

# Define a function to delete a file
def delete_file():
    # Prompt the user to enter the name of the file to delete
    filename = input("Enter the name of the file you want to delete (with extension): ")
    # Check if the file exists
    if os.path.exists(filename):
        # Remove the file using os.remove
        os.remove(filename)
        # Inform the user that the file has been deleted
        print(f"File '{filename}' deleted.")
    else:
        # Inform the user if the file does not exist
        print(f"File '{filename}' does not exist.")

# Define the main function to execute the above functions in sequence
def main():
    create_file()  # Call the create_file function
    read_file()    # Call the read_file function to read the newly created file
    add_content()  # Call the add_content function to add more content to the file
    read_file()    # Call the read_file function again to read the updated content
    delete_file()  # Call the delete_file function to delete the file

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function to start the program