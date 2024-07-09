import os
def create_file():
    filename = input("Enter the name of the file you want to create (with extension): ")
    content = input("Enter the content to insert inside the file: ")
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created and content inserted.")
def read_file():
    filename = input("Enter the name of the file you want to read (with extension): ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    else:
        print(f"File '{filename}' does not exist.")
def add_content():
    filename = input("Enter the name of the file you want to add content to (with extension): ")
    additional_content = input("Enter the new content to add: ")
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            file.write("\n" + additional_content)
        print(f"New content added to '{filename}'.")
    else:
        print(f"File '{filename}' does not exist.")
def delete_file():
    filename = input("Enter the name of the file you want to delete (with extension): ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")
def main():
    create_file()
    read_file()
    add_content()
    read_file()  
    delete_file()
if __name__ == "__main__":
    main()