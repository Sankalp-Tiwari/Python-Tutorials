"""
Iterable - __iter__() or __getitem__()
Iterartor - __next__()
Iterartion -

"""

"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""
# def gen(n):
#     for i in range(n):
#         yield i

# g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

# name = "sankalp"
# p = iter(name)
# for m in p:
#     print(m)


def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac

print(factorial(4))
