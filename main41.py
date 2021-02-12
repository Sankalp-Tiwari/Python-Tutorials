class A:
    classzar = "Class A hai ye"
    def __init__(self):
        self.zar = "This is a var name zar in the constructor of Class A"
        self.classzar = "This is a varzar in Class A"
        self.sp = 'spe'
class B(A):
    classzar = "Class B hai ye"
    def __init__(self):
        super().__init__()
        self.zar = "This is a var name zar in the constructor of Class B"
        self.classzar = "This is a varzar in Class B"
        self.sp = 'sp'

        print(super().classzar)

a = A()
b = B()
print(b.sp)