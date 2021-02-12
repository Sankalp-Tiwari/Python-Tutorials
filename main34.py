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
        """This is an Alternative construction"""
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

aditya = sankalp("Aditya",8,"A")
sankalpq = sankalp("Sankalp",8,"D")
rituraj = sankalp.from_dash("Rituraj-9-C")

aditya.f(5)
print(rituraj.san())