def transform_word(word):
    decrypted = word[::-1]
    encrypted = 'abc' + decrypted + 'xyz'
    return encrypted
def reverse_transform_word(encrypted):
    decrypted = encrypted[3:-3]
    original_word = decrypted[::-1]
    return original_word
word = "hello"
encrypted = transform_word(word)
original_word = reverse_transform_word(encrypted)
print("Original word:", word)
print("encrypted word:", encrypted)
print("Transformed back to original:", original_word)