# def getdate():
#     import datetime
#     return datetime.datetime.now()
print("Type s for sankalp")
print("Type r for rituraj")
print("Type a for aditya")
i = input()
if i=="s":
    print("What do you want to know")
    print("Type e for exercise ")
    print("Type d for diet ")
    io = input()
    if io=="e":
        f = open("sankalpexercise.txt")
        content = f.read()
        print(content)
        f.close()
    if io=="d":
        f1 = open("sankalpdiet.txt")
        content1 = f1.read()
        print(content1)
        f1.close()

if i=="r":
    print("What do you want to know")
    print("Type e for exercise ")
    print("Type d for diet ")
    ioz = input()
    if ioz=="e":
        f2 = open("riturajexercise.txt")
        content2 = f2.read()
        print(content2)
        f2.close()
    if ioz=="d":
        f3 = open("riturajdiet.txt")
        content3 = f3.read()
        print(content3)
        f3.close()
if i=="a":
    print("What do you want to know")
    print("Type e for exercise ")
    print("Type d for diet ")
    iozz = input()
    if iozz=="e":
        f4 = open("adityaex.txt")
        content4 = f4.read()
        print(content4)
        f4.close()
    if iozz == "d":
        f5 = open("adityadiet.txt")
        content5 = f5.read()
        print(content5)
        f5.close()
s = input("press enter to exit\n")