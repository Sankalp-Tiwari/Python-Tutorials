# n = ["34","56","2","12","5"]
# n = list(map(int , n))
# # for i in range(len(n)):
# #     n[i] = int(n[i])
# n[2] = n[2]+5
# print(n)
# def square(x):
#     return x*x
# l1 = [5,6,5,2,8,2,4,5,1,451,44]
# sq = list(map(square,l1))
# print(sq)
# l1 = [5,6,5,2,8,2,4,5,1,451,44]
# cube = list(map(lambda x:x*x*x,l1))
# print(cube)


# def square(a):
#     return a*a
# def cube(x):
#     return x*x
# l1 = [square,cube]
# for i in range(1,11):
#     val = list(map(lambda x:x(i),l1))
#     print("Squre, Cube")
#     print(val)

# ***************************FILTER*****************************************

list_1 = [1,2,4,5,76,78,6,5]
print(list_1)
list_1.sort()
print(list_1)
# def f1(n):
#     return n>5
# l2 = list(filter(f1,list_1))
# print(l2)

# ***************************REDUCE*****************************************

# l1 = [1,2,3,4]
# num = 0
# for i in l1:
#     num = num+i
# print(num)

# from functools import reduce
# l1 = [1,2,3,4]
# num = reduce(lambda x,y:x+y ,l1)
# print(num)