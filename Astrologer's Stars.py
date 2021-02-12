# print("How Many Row You Want To Print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end="")
#         print()

x = int(input("how many rows you want to print\n"))
y = int(input("chose 0 or 1\n"))
# if z==True:
#     for i in range(1, x+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# elif z==False:
#     for i in range(x, 0, -1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# if y==1:
#     for i in range(0,x+1):
#         print("*"*i)
# elif y==0:
#     for i in range(x,0,1):
#         print("*"*i)
a = int(input("enter a number: ")) +1
for i in range(a):
    print("*"*i)
print()
for i in range(a, 0, -1):
    print("*"*i)
