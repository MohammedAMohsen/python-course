# Lesson 021 - Lists
# Video: https://www.youtube.com/watch?v=EpZH9JozUzA

# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "Three", 1, 100.5, True]

print(myAwesomeList)     # ['One', 'Two', 'Three', 1, 100.5, True]
print(myAwesomeList[0])  # One  -> أول عنصر , <class 'str'> نوع الناتج
print(myAwesomeList[-1]) # True -> آخر عنصر
print(myAwesomeList[-3]) # 1

print(myAwesomeList[1:4]) # ['Two', 'Three', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'Three', 1]
print(myAwesomeList[1:])  # ['Two', 'Three', 1, 100.5, True]

print(myAwesomeList[::1]) # ['One', 'Two', 'Three', 1, 100.5, True]
print(myAwesomeList[::2]) # ['One', 'Three', 100.5]
print(myAwesomeList[::3]) # ['One', 1]

# print(myAwesomeList[150]) list index out of range

# ملاحظة: كل سطر هنا يعدّل على القائمة الناتجة من السطر الذي قبله، وليس على القائمة الأصلية
myAwesomeList[1] = 2         # => ['One', 2, 'Three', 1, 100.5, True]
myAwesomeList[-1] = False    # => ['One', 2, 'Three', 1, 100.5, False]
myAwesomeList[2:4] = 3, 10   # => ['One', 2, 3, 10, 100.5, False]
myAwesomeList[0:2] = []      # => [3, 10, 100.5, False]

myAwesomeList[0:3] = ['A', 'B', 'C']   # => ['A', 'B', 'C', False]
myAwesomeList[0:3] = ['A', 'B']        # => ['A', 'B', False]

print(myAwesomeList) # ['A', 'B', False]
