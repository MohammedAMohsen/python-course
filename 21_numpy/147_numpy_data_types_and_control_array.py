# Lesson 147 - Numpy - Data Types And Control Array
# Video: https://www.youtube.com/watch?v=630vRn-VzsM

# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------

import numpy as np

# Sbow Array Data Type

my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.3, 13.35, 61.234])
my_array3 = np.array(["Moh", "AlBasha", "M"])

print(my_array1.dtype) # int64
print(my_array2.dtype) # float64 
print(my_array3.dtype) # <U7 -> (U): Unicode (7): طول اكبر كلمة عندي

# ---------------------------------------------------

# Create Array With Specific Data Type:

my_array4 = np.array([1, 2, 3], dtype=float) # float Or 'float' Or 'f'

my_array5 = np.array([1.3, 13.35, 61.234], dtype=int) # int Or 'int' Or 'i'

# my_array6 = np.array(["Moh", "AlBasha", "M"], dtype= int Or float) # Value Error

print(my_array4.dtype) # float64
print(my_array5.dtype) # int64

# ---------------------------------------------------

# Create Data Type Of Existing Array:

my_array7 = np.array([0, 1, 2, 3, 0, 4])

print(my_array7.dtype) # int64
print(my_array7) # [0 1 2 3 0 4]

my_array7 = my_array7.astype(float) # float Or 'float' Or 'f'

print(my_array7.dtype) # float64
print(my_array7) # [0. 1. 2. 3. 0. 4.]

my_array7 = my_array7.astype(bool) # bool Or 'bool'

print(my_array7.dtype) # bool
print(my_array7) # [False  True  True  True False  True]

# ---------------------------------------------------

# Test Capacity

my_array8 = np.array([100, 200, 400, 300], dtype=float)

print(my_array8.dtype) # float64
print(my_array8[0].itemsize) # 8 Bytes

my_array9 = np.array([100, 200, 400, 300], dtype='f')

print(my_array9.dtype) # float32
print(my_array9[0].itemsize) # 4 Bytes

