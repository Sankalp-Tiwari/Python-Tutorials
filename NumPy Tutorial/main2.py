import numpy as np 

# 0-Dimensional Array
# arr1 = np.array(42)

# 1-Dimensional array
# arr2 = np.array([1,2,3,4,5])

# 2-Dimensional array
# arr3 = np.array([[1,2,3],[4,5,6]])

# 3-Dimensional array
# arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)

# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# print(arr4.ndim)
# ndim tells the dimension of an array

# print(type(arr))
# OUTPUT 
# <class 'numpy.ndarray'>

arr = np.array([1, 2, 3, 4],ndmin=4)
print(arr)
print(arr.ndim)
# ndmin defines the dimension of an array