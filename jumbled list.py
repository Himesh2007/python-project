jumbled_list=[["oongoam","angom","mmanggo"],["orrngea","rangeo","oorange"],["anabaaa","baanaaa","ananab"]]
correct_list=["mango","orange","banana"]
for i in range(len(correct_list)):
    correct_item=correct_list[i]
    sublist=jumbled_list[i]
    for item in sublist:
        if len(correct_item)==len(item):
            print(correct_item,item)
            break