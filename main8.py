"""
i = 0
while (True):
    if i+1<3:
        i = i + 1
        continue

    print(i, end=" ")
    if (i==15):
        i = i + 1
        break
    i = i + 1
"""
while(True):
    p = int(input("enter your number\n"))
    if p>100:
        print("Congratulations You cracked that")
        break
    elif p==100:
        print("you are too close")
        continue
    else:
        print("Better luck next time")
        continue



#                         WHILE LOOP EXTRA
# i= 0
# # while i < 6:
# #  print(i)
# #  while(i<45):
# #      i += 1
# #      if i == 1:
# #          continue
# #      print(i)
# #         #break
#
#
# i = 1
# while i<45:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 45")
#
# # i = 0
# # while i < 6:
# #   i += 1
# #   if i == 3:
# #     continue
# #   print(i)




