# def f1(n):
#     """    :param n
#     :return n! = (n-1)...*1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return  fac
# def f2(n):
#     """
#     :param n
#     :return n! = (n-1)...*1
#      """
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return n * f2(n-1)
#
# # print(f1.__doc__)
# number = int(input("enter the number\n"))
# print("The factorial of your number (" ,number,") using iterative method =",(f1(number)))
# print("The factorial of your number (" ,number,") using recursive method =", (f2(number)))
print("Fibonacchi sequence")
def fibonachi(n):
    """
    :param n: input
    :return: (n-1) + (n-2)
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)

number = int(input("enter the number\n"))
print(fibonachi(number))