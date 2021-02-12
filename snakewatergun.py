import  random
l1 = ["s","w","g"]
noofchances = 10
chances = 0
yourpoint = 0
comppoint = 0
print("Rules\n","Snake+Water=Snake\n","Water+Gun=Water\n","Snake+Gun=Gun")
print("Type s for snake\n","Type w for water\n","Type g for gun")
while(chances<noofchances):
    i = input()
    a = random.choice(l1)
    print("Type s for snake\n", "Type w for water\n", "Type g for gun")
    print("Chance left= ",noofchances-(chances+1))
    if i == a:
        print("you choosed",i,"And computer choosed",a,)
        print("TIE!!!")
    elif i=="s" and a=="w":
        print("you choosed", i, "And computer choosed", a, )
        print("YOU WON !!!")
        yourpoint = yourpoint+1
    elif i=="w" and a=="s":
        print("you choosed", i, "And computer choosed", a, )
        print("COMPUTER WON !!!")
        comppoint = comppoint+1
    elif i=="w" and a=="g":
        print("you choosed", i, "And computer choosed", a, )
        print("YOU WON !!!")
        yourpoint = yourpoint+1
    elif i=="g" and a=="s":
        print("you choosed", i, "And computer choosed", a, )
        print("YOU WON !!!")
        yourpoint = yourpoint+1
    elif i=="g" and a=="w":
        print("you choosed", i, "And computer choosed", a, )
        print("COMPUTER WON !!!")
        comppoint = comppoint+1
    elif i=="s" and a=="g":
        print("you choosed", i, "And computer choosed", a, )
        print("COMPUTER WON !!!")
        comppoint = comppoint+1
    chances = chances+1
    continue
print("GAME OVER!!!")
if comppoint==yourpoint:
    print("TIE\n","YOUR POINT = ",yourpoint,"and computer point = ",comppoint)

if comppoint>yourpoint :
    print("COMPUTER WON\n","Computer point = ",comppoint,"Your point =",yourpoint)
if comppoint<yourpoint :
    print("YOU WON\n","Computer point = ",comppoint,"Your point =",yourpoint)


n = input("Press enter to exit\n")


