# f = open("sankalp1.txt", "w")
# a = f.write("sankalp is a great student\n")
# print(a)
# f.close()
f = open("sankalp1.txt", "r+")
print(f.read(),)
f.write("namastey")
f.close()