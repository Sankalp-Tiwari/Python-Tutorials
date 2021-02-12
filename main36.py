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

class painter(sankalp):
    tofffes = 56
    def __init__(self,zname,zClass,zsec,alanguages):
        self.name = zname
        self.Class = zClass
        self.sec = zsec
        self.language = alanguages

    def print_painter(self):
        return f"Painter's name is {self.name} Total no. of paintings- {self.Class} Role- {self.sec} Languages known {self.language}"


aditya = sankalp("Aditya",8,"A")
sankalpq = sankalp("Sankalp",8,"D")
rituraj = painter("Rituraj",462,"Potraiter",["Hindi"," English","Sanskrit"])
vansh = painter("Vansh",462,"Sketcher",["Hindi"," English","French"])

print(aditya.tofffes)