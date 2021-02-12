class sankalp:
    tofffes = 8

    def __init__(self,zname,zClass,zsec):
        self.name = zname
        self.Class = zClass
        self.sec = zsec

    def san(self):
        return  f"Name is {self.name} Class is {self.Class} Section is {self.sec}"
    @classmethod
    def f(cls,newtoffes):
        cls.tofffes = newtoffes
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def print_good(name):
        print("this is good"+name)

aditya = sankalp("Aditya",8,"A")
sankalpq = sankalp("Sankalp",8,"D")
rituraj = sankalp.from_dash("Rituraj-9-C")

aditya.f(5)
print(rituraj.san())