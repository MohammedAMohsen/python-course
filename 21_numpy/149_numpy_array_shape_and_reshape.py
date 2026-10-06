# Lesson 149 - Numpy - Array Shape And ReShape
# Video: https://www.youtube.com/watch?v=6gmakP7c_UQ

# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

my_array1 = np.array([1, 2, 3, 4])

print(my_array1.ndim) # 1 -> برجع ابعاد المصفوفة
print(my_array1.shape) # (4,) -> برجع عدد العناصر الي في المصفوفة

# -----------------------------------------------

my_array2 = np.array([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ])

print(my_array2.ndim) # 2
print(my_array2.shape) # (3, 4)
# 3 -> ثلاث مصفوفات <- عدد العناصر في البعد الأول 
# 4 -> أربع عناصر <- عدد العناصر في البعد الثاني 

# -----------------------------------------------

my_array3 = np.array([ [ [1, 2, 3, 4, 5], [1, 2, 3, 4, 5] ], [ [1, 2, 3, 4, 5], [1, 2, 3, 4, 5] ] ])

print(my_array3.ndim) # 3
print(my_array3.shape) # (2, 2, 5)

# -----------------------------------------------

my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(my_array4.ndim) # 1
print(my_array4.shape) # (12,)

reshaped_array4 = my_array4.reshape(2, 6)

print(reshaped_array4) # [ [ 1  2  3  4  5  6] [ 7  8  9 10 11 12] ]
print(reshaped_array4.ndim) # 2
print(reshaped_array4.shape) # (2, 6)

reshaped_array5 = my_array4.reshape(3, 4)

print(reshaped_array5) # [ [ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12] ]
print(reshaped_array5.ndim) # 2
print(reshaped_array5.shape) # (3, 4)

reshaped_array6 = my_array4.reshape(3, 2, 2)

print(reshaped_array6) # [ [ [1  2] [3  4] ] [ [5  6] [7  8] ] [ [9 10] [11 12] ] ]
print(reshaped_array6.ndim) # 3
print(reshaped_array6.shape) # (3, 2, 2)

# -----------------------------------------------

my_array7 = np.array([ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ])

print(my_array7.ndim) # 2
print(my_array7.shape) # (2, 10)

reshaped_array7 = my_array7.reshape(-1) # برجع المصفوفة لبعد واحد مهما كان أبعاد المصفوفة

print(reshaped_array7) # [ 1  2  3  4  5  6  7  8  9 10  1  2  3  4  5  6  7  8  9 10]
print(reshaped_array7.ndim) # 1
print(reshaped_array7.shape) # (20,)

# -------------------

reshaped_array8 = my_array7.reshape(5, 4)

print(reshaped_array8) # [ [ 1  2  3  4] [ 5  6  7  8] [ 9 10  1  2] [ 3  4  5  6] [ 7  8  9 10] ]
print(reshaped_array8.ndim) # 2
print(reshaped_array8.shape) # (5, 4)
