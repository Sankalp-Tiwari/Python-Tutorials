class A:
    def print(self):
        return f"This is a function in class A"
class B(A):
    def print(self):
        return f"This is a function in class B"

class C(A):
    def print(self):
        return f"This is a function in class C"
class D(C,B):
    def print(self):
        return f"This is a function in class D"

a = A()
b = B()
c = C()
d = D()

print(d.print())