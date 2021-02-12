# it is an faulty calculator this made so that no one can cheat
#the following questions are asked in exams:-
#56+9 or 9+56
#45+3 or 3*45
#56/6
#there answers will be like this:-
#56+9 or 9+56 = 77
#45+3 or 3*45 =555
#56/6 = 4
#if any other question is asked this calculator will answer this correctly
print("PLEASE SELECT AN OPERATOR +, -, *, /")
o = input()
print("ENTER YOUR 1st NUMBER")
n1 = int(input())
print("ENTER YOUR 2nd NUMBER")
n2 = int(input())


if o=="+":
   if n1==56 and n2 ==9 or n1==9 and n2 ==56:
       print("77")
   else:
       print(n1+n2)

elif o=="-":
    print(n1-n2)

elif o=="*":
    if n1==45 and n2 ==3 or n1==3 and n2 ==45:
        print("555")
    else:
        print(n1*n2)

elif o=="/":
    if n1 == 56 and n2 == 6 :
        print("4")
    else:
        print(n1/n2)

print("press enter to exit ")

q = input()


