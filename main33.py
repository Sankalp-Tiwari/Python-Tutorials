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

aditya = sankalp("Aditya",8,"A")
sankalpq = sankalp("Sankalp",8,"D")
# sankalp.tofffes = 7
aditya.f(5)
print(aditya.tofffes)
