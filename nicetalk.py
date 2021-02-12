import random

name = input("Enter your name\n")

gender = input("Enter your gender (f for female,m for male)\n")

if gender == "f" or "F":
    heshe = "she"
    hisher = "her"
    boygirl = "girl"
    himher = "her"

elif gender == "m" or "M":
    heshe = "he"
    hisher = "his"
    boygirl = "boy"
    himher = "him"

facts = [f"{name} is a very good person. {heshe} nor enlighten {himher}self {heshe} also enlighten {hisher} friends",
         f"{name} is just fantastic {boygirl}.{heshe}{hisher}", f"{name}{heshe}{hisher}", f"{name}{heshe}{hisher}", f"{name}{heshe}{hisher}"]

# randmozing fact by setting a varialble a
a = random.choice(facts)
print(a)

