
def f1(str):
    return f"Hi this is your name {str}"
str = input("enter your name\n")

def f2(n1,n2):
    return n1+n2+5
n1 = int(input("enter your number\n"))
n2 = int(input("enter your second number\n"))

if __name__ == '__main__':

    print(f1(str))
    print(f"And sum of your numbers =", f2(n1,n2))