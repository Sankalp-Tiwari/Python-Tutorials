# def minus(x,y):
#     print(x-y)
#     return x,y
# minus = lambda x,y:x-y
# x = int(input("enter the first number\n"))
# y = int(input("enter the second number\n"))
# # print(minus(x,y))
# def a_sortw(a):
#     return a[1]

a = [[45,12,23],[9,6,67],[99,1,6]]
a.sort(key=lambda x:x[0])
print(a)