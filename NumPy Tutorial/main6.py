# .copy() - it copies the original array and any changes made to it will not affect
#  original array and any changes made to original array will not affect it
# .view() - it view the original array and any changes made to it will affect
#  original array and any changes made to original array will affect it

import numpy as np 


# COPY
# arr = np.array([1,2,3,4,5,6])
# x = arr.copy()
# arr[0] = 42
# print(arr[0])
# print(x[0])

# VIEW
# arr = np.array([1,2,3,4,5,6])
# x = arr.view()
# arr[0] = 42
# print(arr[0])
# print(x[0])
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31

# print(arr)
# print(x)



# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

print(x.base) # Will return None
print(y.base) # will return the original array