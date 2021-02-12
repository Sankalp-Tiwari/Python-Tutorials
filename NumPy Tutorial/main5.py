# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# The NumPy array object has a property called dtype that returns the data type of the array

import numpy as np 

# arr = np.array([1, 2, 3, 4], dtype='i4')
# arr1 = np.array(["Sankalp","Pragalbha"], dtype='S')
# arr2 = np.array(['1', '2', '3'], dtype='i') # We can convert an string value to an integer with dtype=i and so on...

# arr2 = np.array(['a', '2', '3'], dtype='i')
# It will raise an error because all are string not integer      ||valueerror

# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# newarr = arr.astype(int)
newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)




# print(arr.dtype)
# print(arr1.dtype)
# print(arr2.dtype)