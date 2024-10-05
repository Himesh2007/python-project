def decor(func):
    def inner():
        print("Change value of a")
        a = func()  # Call the passed function
        a = a + 5
        return a
    return inner

def original_sum():
    return 10

decorated_sum = decor(original_sum)  # Pass the function reference without calling it
print(decorated_sum())  # Call the decorated function