todo_list = {}
def add_task():
    title = input("Enter the task title: ")
    desc = input("Enter the task description: ")
    todo_list[title] = desc
    print(f"Task '{title}' added.")
def view_tasks():
    if todo_list:
        print("To-Do List:")
        for title, desc in todo_list.items():
            print(f"Title: {title}, Description: {desc}")
    else:
        print("To-Do list is empty.")
def delete_task():
    title = input("Enter the task title you want to delete: ")
    if title in todo_list:
        del todo_list[title]
        print(f"Task '{title}' deleted.")
    else:
        print(f"Task '{title}' not found.")
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()