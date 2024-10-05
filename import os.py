import os  # Import the os module for interacting with the operating system

a = "hi"  # Define a directory name
location = "C:/Users/himes/OneDrive/Desktop/New folder (2)"  # Define the path where the new directory will be created

# Join the location and directory name to create the full path
path = os.path.join(location, a)

# Create a new directory at the specified path
os.mkdir(path)