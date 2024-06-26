def max(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
l = [20, 30, 40, 50, 15, 10]
print("Largest element is:", max(l))