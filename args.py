def abc(*args):
        sum = 0
        for num in args:
            sum = sum + num
        return sum
sum = abc(2,3,4,5,6,7)
print (sum)
sum = abc(3,4,5)
print (sum)