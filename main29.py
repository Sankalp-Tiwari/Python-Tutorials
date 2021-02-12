# import time
# def func1():
#     print("Excecuting now")
#     time.sleep(1)
#     print("Executed...")
# func2 = func1
# del func1
# func2()
# a = time.gmtime(0)
# print(a)


# def f1(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# x = f1(1)
# print(x)

# def exc(func):
#     func("Sankalp")
# exc(print)
# import time
# def dec(func1):
#     def executor():
#         print("Executing Now...")
#         time.sleep(2)
#         func1()
#         print("Executed")
#     return executor()
# @dec
# def sankalp():
#     print("Sankalp studies in class 8")
#
# # sanki = dec(sanki)
#
# sankalp()
# import time
# def inner1(func):
#     def inner2():
#         print("Before function execution")
#         time.sleep(2)
#         func()
#         print("After function execution")
#     return inner2
#
# @inner1
# def function_to_be_used():
#     print("This is inside the function")
#
# function_to_be_used()
#
def dec(function):
    def excecutor():
        print("Executing now...")
        function()
        print("Executed")
    return excecutor
@dec
def sankalp():
    print("sankalp studies in class 8")
# sankalp = dec(sankalp)
sankalp()