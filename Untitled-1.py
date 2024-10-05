fruit = ["apple", "banana", "mango", "grape", "gauva"]  # List of fruits
for i in fruit:  # Loop through each fruit in the list
    for letter in i:  # Loop through each letter in the current fruit's name
        if letter in ("a", "e", "i", "o", "u"):  # Check if the letter is a vowel
            print(i, letter)  # Print the fruit and the vowel found
# The line print(i=letter) is incorrect syntax and has been removed