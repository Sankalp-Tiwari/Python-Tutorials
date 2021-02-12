# class Student:
#     tofffes = 8
#
#     def __init__(self,zname,zClass,zsec):
#         self.name = zname
#         self.Class = zClass
#         self.sec = zsec
#
#     def san(self):
#         return  f"Name is {self.name} Class is {self.Class} Section is {self.sec}"
#     @classmethod
#     def f(cls,newtoffes):
#         cls.tofffes = newtoffes
#     def __truediv__(self, other):
#         return self.Class / other.Class
#
# stu1 = Student("Sankalp",8,"D")
# stu2 = Student("Aditya",8,"D")
# print(stu1/stu2)
class A:
    def __init__(self,name,number):
        self.name = name
        self.number=number
    def print_info(self):
        return f"The name is {self.name} Number is {self.number}"
    def __repr__(self):
        return f"('{self.name},{self.number}')"
    def __str__(self):
        return f"Name is {self.name} no. is {self.number}"
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split(","))

stu = A.from_dash("Sankalp,56")
print(stu)