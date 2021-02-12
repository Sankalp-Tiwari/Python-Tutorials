'''
Author : Sankalp
Date : 23 January 2021
Purpose : Practise Problem
'''
mylist = []
no_of_items = int(input("Enter the size of the list\n"))
for i in range(no_of_items):
    list_item = input("Enter the item of the list\n")
    mylist.append(list_item)

reverseList1 = mylist.copy()
reverseList1.reverse()
print(f"The Original List = {mylist} The Reversed List = {reverseList1}")
reverseList2 = mylist.copy()
print(f"The Original List = {mylist} The Reversed List = {reverseList2[::-1]}")

reverseList3 = mylist.copy()
for i in range(len(reverseList3)//2):
    reverseList3[i], reverseList3[len(reverseList3)-i-1] = reverseList3[len(reverseList3)-i-1],reverseList3[i]

print(f"The Original List = {mylist} The Reversed List = {reverseList3}")