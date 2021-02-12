class sankalp:
    tofffes = 8

    def __init__(self,zname,zClass,zsec):
        self.name = zname
        self.Class = zClass
        self.sec = zsec

    def san(self):
        return  f"Name is {self.name} Class is {self.Class} Section is {self.sec}"
aditya = sankalp("Sankalp",8,"D")
# sankalpq = sankalp()

# sankalpq.name = "Sankalp"
# sankalpq.Class = 8
# sankalpq.sec = "D"
#
# aditya.name = "Aditya"
# aditya.Class = 8
# aditya.sec = "A"

print(aditya.san())


# class Employee:
#     no_of_leaves = 8
#
#     # def __init__(self, aname, asalary, arole):
#     #     self.name = aname
#     #     self.salary = asalary
#     #     self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#
# # harry = Employee("Harry", 255, "Instructor")
#
# rohan = Employee()
# harry = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(harry.printdetails())

