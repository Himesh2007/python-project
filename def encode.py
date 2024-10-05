# Define a function to transform a word by reversing it and adding 'abc' and 'xyz'
def transform_word(word):
    # Reverse the input word
    decrypted = word[::-1]
    # Create an encrypted version by adding 'abc' at the start and 'xyz' at the end
    encrypted = 'abc' + decrypted + 'xyz'
    # Return the encrypted word
    return encrypted

# Define a function to reverse the transformation and get back the original word
def reverse_transform_word(encrypted):
    # Remove the 'abc' from the start and 'xyz' from the end to get the reversed word
    decrypted = encrypted[3:-3]
    # Reverse the decrypted word to get the original word
    original_word = decrypted[::-1]
    # Return the original word
    return original_word

# Define the original word
word = "hello"
# Transform the word
encrypted = transform_word(word)
# Reverse the transformation to get the original word back
original_word = reverse_transform_word(encrypted)

# Print the original word
print("Original word:", word)
# Print the encrypted word
print("Encrypted word:", encrypted)
# Print the transformed back original word
print("Transformed back to original:", original_word)