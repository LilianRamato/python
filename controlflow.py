marks=int(input("weka alama yako:"))
# if elif else statement
if marks>80 and marks<=100:
    print("you scored an A")
elif marks>60 and marks<=80:
    print("you have  a B....")
elif marks>40 and marks<=60:
    print("you have  a C...")
elif marks>30 and marks<=40:
    print("you have a D...")
elif marks>=0 and marks<=30:
    print("you have an E")
else:
    print("wrong input")
