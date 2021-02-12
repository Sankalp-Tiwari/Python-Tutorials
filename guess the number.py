"""
n = 7
u = 1
while(u<=5):
    i = int(input("enter your number\n"))

    if i<n:
        print("you are low")
        continue
    elif i>n:
        print("you are high")
        continue
    else:
        print("you took ", u,"guesses",  "you won ")
if u>9:
    print("game over")
"""
n = 7
u = 0
print("number of guesses left = 5")
while(u<=5):
    o = int(input("enter you number\n"))
    if o<7:
        print("you are low")
    elif o>7:
        print("you are high")
    else:
        print("you won!")
        print(u, "no. of guesses you took")
        break
    print(5-u, "no. of gusses left")
    u = u + 1

if(u>5):
    print("game over")
ex = input("press enter to exit")