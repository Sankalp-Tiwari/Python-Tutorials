import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a = arr.reshape(4,3)
# a = arr.reshape(2,3,2)

# arr = np.array([1,2,3,4,5,6,7,8])
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
# a = arr.reshape(2,3,3)
# a = arr.reshape(2,3,-1)
# print(a)
# print(a.base) # Returns a view not copy


# MULTIDIMENSIONAL ARRAY TO 1-DIMENSIONAL ARRAY
arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
a = arr.reshape(-1)
print(a)

# Note: There are a lot of functions for changing the
#  shapes of arrays in numpy flatten, ravel and also 
# for rearranging the elements rot90, flip, fliplr, flipud 
# etc. These fall under Intermediate to Advanced section of numpy.