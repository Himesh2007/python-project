a=input()
if a.startswith("displaygarnus(\"") and a.endswith("\")"):
                print(a[15:-2])
elif a.startswith("displaygarnus(") and a.endswith(")"):
        print(eval(a[14:-1]))
# from display import displaygarnus
# if a.startswith("displaygarnus(\"") and a.endswith("\")"):
#     displaygarnus(a[15:-2])
# elif a.endswith("displaygarnus(") and a.endswith(")"):
#     displaygarnus(eval(a{14:-1}))