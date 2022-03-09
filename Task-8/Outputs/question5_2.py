import numpy as np

arr_1 = np.random.randint(0,3,6)   # Producing two random numpy arrays.
arr_2 = np.random.randint(0,3,6)

print(arr_1)
print(arr_2)
print(np.where(arr_1 == arr_2))   # Calling where() function to print the indexes of same elements.
