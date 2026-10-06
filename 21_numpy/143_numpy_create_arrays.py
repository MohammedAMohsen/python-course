# Lesson 143 - Numpy - Create Arrays
# Video: https://www.youtube.com/watch?v=vGJxavinB9M

# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------

import numpy as np

# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

# Print

print(my_list) # [1, 2, 3, 4, 5]
print(my_array) # [1 2 3 4 5]

# Type

print(type(my_list)) # <class 'list'>
print(type(my_array)) # <class 'numpy.ndarray'> ndarray -> (n): number (d): dimensional array

# Accessing Elements

print(my_list[0]) # 1
print(my_array[0]) # 1

# Type Number Dimensional Array

a = np.array(10) # -> This is 0 Dimensional Array
b = np.array([10, 20]) # ->  This is 1 Dimensional Array
c = np.array( [[1, 2], [3, 4], [5, 6]] ) # ->  This is 2 Dimensional Array
d = np.array( [ [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ] ] ) # ->  This is 3 Dimensional Array

print(d[1]) # [[5 6] [7 8]]
print(d[1][1]) # [7 8]
print(d[1][1][1]) # 8
print(d[1,1,1]) # 8
print(d[1,1,-1]) # 8

# Number Of Dimensional

print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

# Custom Dimensional

my_custom_array = np.array([1, 2, 3], ndmin=3)

print(my_custom_array) # [[[1 2 3]]]
print(my_custom_array.ndim) # 3

print(my_custom_array[0]) # [[1 2 3]]
print(my_custom_array[0, 0]) # [1 2 3]
print(my_custom_array[0, 0, 0]) # 1

# print(my_custom_array[1]) # Error
