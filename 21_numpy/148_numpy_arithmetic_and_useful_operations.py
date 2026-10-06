# Lesson 148 - Numpy - Arithmetic And Useful Operations
# Video: https://www.youtube.com/watch?v=QbHFEo-YAPU

# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------
import numpy as np

my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])

print(my_array1 + my_array2) # [15 22 34]

print(my_array1 - my_array2) # [ 5 18 26]

print(my_array1 * my_array2) # [ 50  40 120]

print(my_array1 / my_array2) # [ 2.  10.   7.5]

# ---------------------------------------------------

my_array3 = np.array([ [1, 4], [5, 9] ])
my_array4 = np.array([ [2, 7], [10, 5] ])

print(my_array3 + my_array4) # [ [ 3 11] [15 14] ]

print(my_array3 - my_array4) # [ [-1 -3] [-5  4] ]

print(my_array3 * my_array4) # [ [ 2 28] [50 45] ]

print(my_array3 / my_array4) # [ [0.5 0.57142857] [0.5 1.8] ]

# ---------------------------------------------------

# min , max , sum

my_array5 = np.array([10, 20, 30])

print(my_array5.min()) # 10
print(my_array5.max()) # 30
print(my_array5.sum()) # 60

my_array6 = np.array([ [6, 4], [3, 9] ])

print(my_array6.min()) # 3
print(my_array6.max()) # 9
print(my_array6.sum()) # 22

# ---------------------------------------------------

# Ravel

my_array7 = np.array([ [6, 4], [3, 9] ])
my_array8 = np.array([ [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ] ])

print(my_array7.ravel()) # [6 4 3 9]
print(my_array8.ravel()) # [1 2 3 4 5 6 7 8]

