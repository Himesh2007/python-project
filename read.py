# Open the file 'execption.txt' in read mode
with open('execption.txt', 'r') as file:
    file_read = file.read()  # Read the entire content of the file into the variable 'file_read'
    print(file_read)  # Print the content read from the file
    # No need to explicitly close the file as 'with' statement handles it
    # file.close()  # This line is redundant and can be omitted