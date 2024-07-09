# sub = {"maths":21, "science":22}
def percentage(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum = sum + value
    return sum
sum = percentage(math=99, english=79)
print (sum)