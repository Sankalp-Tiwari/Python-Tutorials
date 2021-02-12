class Google:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.email = f"{self.name}{self.lastname}@gmail.com"
    def print_name(self):
        return f'Name is {self.name} {self.lastname}'
    @property
    def print_email(self):
        if self.name == None or self.lastname == None:
            return ("Email is deleted")
        else:
            return f"{self.name}:{self.lastname}@gmail.com"
    @print_email.setter
    def print_email(self,str):
        naam = str.split("@")[0]
        self.name = naam.split(":")[0]
        self.lastname = naam.split(":")[1]
    @print_email.deleter
    def print_email(self):
        self.name = None
        self.lastname = None

sankalp = Google("Sankalp","Tiwari")
print(sankalp.email)
sankalp.name = "sankalp"
sankalp.lastname = "tiwari"
print(sankalp.print_email)
sankalp.print_email = "7815sankalp:tiwari8d@gmail.com"
print(sankalp.name)
del sankalp.print_email
print(sankalp.print_email)