# Lesson 144 - Numpy - Compare Data Location And Type
# Video: https://www.youtube.com/watch?v=5rkKhsdJ0UU

# ---------------------------------------------
# -- Numpy => Compare Data Location And Type --
# ---------------------------------------------

import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0]) # 1
print(my_list[1]) # 2

print(my_array[0]) # 1
print(my_array[1]) # 2


# أرقام العناوين التالية تختلف من جهاز لآخر ومن تشغيل لآخر
print(id(my_list[0])) # 11755688
print(id(my_list[1])) # 11755720

print(id(my_array[0])) # 133518651702736
print(id(my_array[1])) # 124154190577392

my_list_of_data = [1, 2, 'A', 'B', True, 10.43] # غير متجانسة
my_array_of_data = np.array([1, 2, 'A', 'B', True, 10.43]) # غير متجانسة

print(my_list_of_data) # [1, 2, 'A', 'B', True, 10.43] => --Heterogeneous -> تعامل مع البيانات على انها غير متجانسة
print(my_array_of_data) # ['1' '2' 'A' 'B' 'True' '10.43'] => Homogeneous-> تعامل مع البيانات على انها نوع واحد وهو نص

print(type(my_list_of_data[0])) # <class 'int'>
print(type(my_array_of_data[0])) # <class 'numpy.str_'>

# ---------------

my_array_of_data_two = np.array([1, 2]) # متجانسة

print(my_array_of_data_two) # [1 2] -> عشان البيانات من الأصل متجانسة تعامل معها على نوعها الأساسي وما غيرها

print(type(my_array_of_data_two[0])) # <class 'numpy.int64'>

# ----------------

my_array_of_data_three = np.array([1, 2, 6.43]) # غير متجانسة

print(my_array_of_data_three) # [1.   2.   6.43] -> وأصبحت متجانسة Float حول البيانات لانها غير متجانسة على ان كل البيانات عبارة عن 

print(type(my_array_of_data_three[0])) # <class 'numpy.float64'>
