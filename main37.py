class sankalp:
    tofffes = 8
    f8 = 65
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
class sports:
    f8 = 20
    def __init__(self,name,sports):
        self.name = name
        self.sports = sports

    def print_player(self):
        return f"Players name is {self.name} Sports played by him {self.sports}"
class cool_student(sports,sankalp):
    # f8 = 100
    lang = "Sanskrit"
    def langa(self):
        print(self.lang)
        return self.lang
aditya = sankalp("Aditya",8,"A")
sankalpq = sankalp("Sankalp",8,"D")
vansh = sports("Vansh",["Cricket","Football"])
rituaraj = sports("Ritraj",["Tennis"])

des = rituaraj.f8
print(des)