import numpy as np

# NumPy arrays have an attribute called shape that returns a 
# tuple with each index having the number of corresponding elements.
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape) #returns (2, 4), which means that the array has 2 dimensions, and each dimension has 4 elements



arr = np.array([1,2,3,4],ndmin=5)
print(f"array's shape = {arr.shape}")