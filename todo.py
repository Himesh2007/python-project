# Define a global dictionary to store tasks
todo_list = {}

# Function to add a task to the to-do list
def add_task():
    title = input("Enter the task title: ")  # Prompt user to enter the task title
    desc = input("Enter the task description: ")  # Prompt user to enter the task description
    todo_list[title] = desc  # Add the task title and description to the dictionary
    print(f"Task '{title}' added.")  # Confirm that the task has been added

# Function to view all tasks in the to-do list
def view_tasks():
    if todo_list:  # Check if the dictionary is not empty
        print("To-Do List:")  # Print the header for the to-do list
        for title, desc in todo_list.items():  # Iterate through the dictionary items
            print(f"Title: {title}, Description: {desc}")  # Print each task's title and description
    else:  # If the dictionary is empty
        print("To-Do list is empty.")  # Inform the user that the to-do list is empty

# Function to delete a task from the to-do list
def delete_task():
    title = input("Enter the task title you want to delete: ")  # Prompt user to enter the task title to delete
    if title in todo_list:  # Check if the task title exists in the dictionary
        del todo_list[title]  # Delete the task from the dictionary
        print(f"Task '{title}' deleted.")  # Confirm that the task has been deleted
    else:  # If the task title does not exist in the dictionary
        print(f"Task '{title}' not found.")  # Inform the user that the task was not found

# Main function to display the menu and handle user choices
def main():
    while True:  # Loop to repeatedly display the menu
        print("\nTo-Do List Menu:")  # Print the menu header
        print("1. Add Task")  # Option to add a task
        print("2. View Tasks")  # Option to view tasks
        print("3. Delete Task")  # Option to delete a task
        print("4. Exit")  # Option to exit the program
        choice = input("Enter your choice: ")  # Prompt user to enter their choice
        if choice == '1':  # If user chooses to add a task
            add_task()  # Call the add_task function
        elif choice == '2':  # If user chooses to view tasks
            view_tasks()  # Call the view_tasks function
        elif choice == '3':  # If user chooses to delete a task
            delete_task()  # Call the delete_task function
        elif choice == '4':  # If user chooses to exit
            break  # Exit the loop and end the program
        else:  # If user enters an invalid choice
            print("Invalid choice. Please try again.")  # Inform the user and prompt again

# Check if the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function to start the program