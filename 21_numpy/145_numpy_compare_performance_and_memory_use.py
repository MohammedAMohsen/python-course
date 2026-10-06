# Lesson 145 - Numpy - Compare Performance And Memory Use
# Video: https://www.youtube.com/watch?v=koMDndoAvCc

# -------------------------------------------------
# -- Numpy => Compare Performance And Memory Use --
# -------------------------------------------------
# - Performance
# - Memory Use
# -------------------------------------------------

import numpy as np
import time
import sys

elements = 10_000_000 # عشرة ملايين عنصر
# تحذير: لا تكبر هذا الرقم كثيرا، فالقائمة الكبيرة تستهلك ذاكرة ضخمة وقد يتجمد جهازك

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

# -----------------------------------------------------------------------------------
# جمع العنصر الأول في القائمة الأولى بالعنصر الأول في القائمة الثانية وهكذا ... للآخر
# -----------------------------------------------------------------------------------

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]

# print(list_result) # [0, 2, 4, 6, ...]

print(f"List Time: {time.time() - list_start:.2f}s") # List Time: 1.30s -> الوقت يختلف حسب جهازك

# -------------------------------------------------------------------------------------
# جمع العنصر الأول في المصفوفة الأولى بالعنصر الأول في المصفوفة الثانية وهكذا ... للآخر
# -------------------------------------------------------------------------------------

array_start = time.time()
array_result = my_array1 + my_array2

# print(array_result) # [0 2 4 6 ...]

print(f"Array Time: {time.time() - array_start:.2f}s") # Array Time: 0.09s -> أسرع بحوالي 14 مرة

# --------------------------------------------------------------
# النتائج صادمة سواء في طريقة كتابة العملية او في الوقت المستهلك
# --------------------------------------------------------------

my_array = np.arange(100)

print(my_array)
print(my_array.itemsize) # 8 -> حجم العناصر بالبايت
print(my_array.size) # 100 ->  حجم المصفوفة
print(f"All Bytes: {my_array.itemsize * my_array.size}") # All Bytes: 800

my_list = range(100)

print(sys.getsizeof(1)) # 28 -> حجم العناصر بالبايت
print(len(my_list)) # 100 ->  حجم القائمة
print(f"All Bytes: {sys.getsizeof(1) * len(my_list)}") # All Bytes: 2800
# والحجم الحقيقي للقائمة أكبر من ذلك، لأنها تحفظ أيضا عنوانا بحجم 8 بايت لكل عنصر

# ---------------------------------------------------------------
# حتى في الحجم المصفوفة اخف بكثير من القائمة واقل استعمال للذاكرة
# ---------------------------------------------------------------
