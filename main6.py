l1 = [["sankalp",4],["pragalbha",9], ["shubham",60]]
d1 = dict(l1)
for items in d1:
    print(items)
print(l1)
print(d1)
for item, candy in d1.items():
    print(item, candy)

l1 = ["sankalp", 3, 44,55, 55, 12, 6, 5]
for items in l1:
    if str(items).isnumeric() and items>=6:
        print(items)

print("press enter to exit")
nh = input()

#                                             FOR LOOPS EXTRA
# l1 = ["sankalp","pragalbha","aditya","rituraj"]
# runs = ["23","0","100","49"]
# # for player in l1:
# #     # print(player)
# #     if player=="aditya":
# #         continue
# #     print(player)
# # for i in range(1,6):
# #     print(i)
# # else:
# #     print("Thats all!")
# # for x in l1:
# #     for y in runs:
# #         print(x,y)
# for a in [0,1,2,3]:
#     pass
#      # (having an empty for loop like this, would raise an error without the pass statement)