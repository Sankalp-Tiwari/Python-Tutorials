#GLOBAL VARIABLES
year = 2021
yearage = int(input("Enter your age or year of birth\n"))
if yearage<999:
        #age
        if yearage>120:
            print("You seem to be oldest person alive!!")
        elif yearage<-999:
            print("your age is in minus")
        else:
            wishedYear = int(input("Enter the year you want to know your age\n"))
            bornYear = year-yearage
            wishedYear1 = wishedYear-bornYear
            if wishedYear>year:
                print(f"you will be {wishedYear1} year old in {wishedYear}")
            else:
                print("please choose the correct year")

elif yearage>1000:
        #year
        if yearage<1939:
            print("you seem to be oldest person alive")
        elif yearage>year:
            print("you havenot born yet!!")
        else:
            wishedYear = int(input("Enter the year you want to know your age\n"))
            age = year-yearage
            wishedYear1 = (wishedYear-year)+age
            if wishedYear>year:
                print(f"you will be {wishedYear1} year old in {wishedYear}")
            else:
                print("Please choose correct year")