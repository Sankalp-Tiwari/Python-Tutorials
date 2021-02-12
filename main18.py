# def harry():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#         print("Before calling rohan",x)
#         rohan()
#         print("After calling rohan",x)
# harry()

# def harry():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#     print("before calling rohan()", x)
#     rohan()
#     print("after calling rohan()", x)
#
# harry()
# def print_msg(msg):
#     # This is the outer enclosing function
#
#     def printer():
#         # This is the nested function
#         print(msg)
#
#     printer()
#
# # We execute the function
# # Output: Hello
# print_msg("Hello World")
# def print_func(msg):
#     def printer():
#         print(msg)
#     printer()
# print_func("Hello world")
def sankalp():
    x = 20
    def aditya():
        global x
        x = 50
    print("Before calling aditya()", x)
    aditya()
    print("After calling aditya()", x)

sankalp()