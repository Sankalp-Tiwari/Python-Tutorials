from abc import ABCMeta,abstractmethod
i = int(input("Enter the length of rectangle"))
i2 = int(input("Enter the breadth of rectangle"))
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type = "rectangle"
    side = 4
    def __init__(self):
        self.len = i
        self.bred = i2
    def printarea(self):
        return f"The area of the rectangle = {self.len*self.bred}"
rect = Rectangle()
print(rect.printarea())

