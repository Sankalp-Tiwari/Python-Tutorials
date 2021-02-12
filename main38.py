class electronic_device():
    electricity = ["AC(Cannot be stored)","DC(Can be stored)"]
    def elec(self):
        return f"I like both types elctricity {self.electricity}"
class pocket_gadjet(electronic_device):
    electricity = 0
    def elec(self):
        return f"I dont like electicity {self.electricity}"
class phone(pocket_gadjet):
    electricity = "DC(Can be stored)"
    def elec(self):
        return f"I like only 1 type of electricity {self.electricity}"

electronic__device = electronic_device()
pocket__gadjet = pocket_gadjet()
phone__ = phone()
print(phone__.elec())