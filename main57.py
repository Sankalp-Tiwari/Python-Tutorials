# a = input("What is your name")
# b = int(input("Kitna kamalete ho"))
#
# if b==0:
#     raise ZeroDivisionError("pagal 0 kyu daala")
# if a.isnumeric():
#     raise Exception ("numbers are not allowed")
# print(f"hello {a}")

i = input("Enter your name\n")
try:
    print(a)
except Exception as e:
    if i=="sankalp" or "Sankalp" or "SANKALP":
        raise ValueError("CRIMINAL!!!")

    print("exception handellled")