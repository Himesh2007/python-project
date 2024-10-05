# Open the file named 'execption.txt' in read mode
file = open('execption.txt')

# Read the entire content of the file
file_read = file.read()

# Print the content read from the file
print(file_read)

# Close the file to release system resources
file.close()