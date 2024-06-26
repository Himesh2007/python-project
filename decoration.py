def decor(sum):
    def inner ():
        print("change value of a")
        a = sum
        a = a+5
        return a
    return inner
def sum():  
    return 10
sum = decor(sum())
print(sum())