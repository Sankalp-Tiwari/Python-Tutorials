class Library:
    def __init__(self,name,booklist):
        self.name = name
        self.booklist = booklist
        self.lenddict = {}
    def displaybook(self):
        print(f"The books we currently have are")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("You can take this book")
        else:
            print(f"This book already being used by {self.lenddict[book]}")
    def returnbook(self,book):
        self.lenddict.pop(book)
        print("thanks")
    def addbook(self,book):
        self.booklist.append(book)
        print("The book has been updated")
if __name__ == '__main__':
    sankalp = Library("Sankalp's Library",['Harry Porter','Universal Science'])
    while True:
        print(f"Welcome to your library{sankalp.name}")
        print("What do you want to do?")
        print("1: display a book")
        print("2: lend a book")
        print("3: add a book")
        print("4: return a book")
        userchoice = input()
        if userchoice=='1':
            sankalp.displaybook()
        elif userchoice=='2':
            book = input("Enter the name of the book you want to lend")
            username = input("Enter your name")
            sankalp.lendbook(username,book)
        elif userchoice=='3':
            book = input("Enter the name of the book you want to add")
            sankalp.addbook(book)
        elif userchoice=='4':
            book = input("Enter the name of the book you want to return")
            sankalp.returnbook(book)
        else:
            print("You gave us wrong input!!")
        print("Enter c to continue and q to quit")
        a = input()
        if a=="c":
            continue
        elif a=="q":
            exit()