# three_list_tables = [i for i in range(100) if i%3==0]
# print(three_list_tables)

# dresses = {dress for dress in ["dress1","dress2","dress1","dress1","dress2","dress3","dress1"]}
# print(dresses)

# evens = (i for i in range(101) if i%2==0)
# for item in evens:
#     print(item)

Input = int(input("How many items you want to add\n"))
List = []
for i in range(1,Input+1):
    Input_2 = input("Enter the items you want to enter\n")
    List.append(Input_2)

Input_3 = input("You want to make list comprehesion,set comprehesion,dictionary comprehesion\n"
                "Type list for list comprehesion\n"
                "Type set for set comprehesion\n"
                "Type dict for dictonary comprehesion\n")
if Input_3=="list":
    for i in List:
        print(i)
elif Input_3=="set":
    List = {i for i in List}
    print(List)
elif Input_3=="dict":
    List = {f"item{i}":i for i in List}
    print(List)