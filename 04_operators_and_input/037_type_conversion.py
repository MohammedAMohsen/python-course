# Lesson 037 - Type Conversion
# Video: https://www.youtube.com/watch?v=j26DuY69HYA

# ---------------------
# -- Type Conversion --
# ----------------------

# str() -> بحول لنص

a = 10

print(type(a)) # <class 'int'>
print(type(str(a))) # <class 'str'>

# tuple()

c = "Mohammed"                   # -> String
d = [1, 2, 3, 4, 5]              # -> List
e = {"A", "B", "C"}              # -> set
f = {"A": 1, "B": 2, "C": 3}     # -> Dictionary

print(tuple(c)) # ('M', 'o', 'h', 'a', 'm', 'm', 'e', 'd')
print(tuple(d)) # (1, 2, 3, 4, 5)
print(tuple(e)) # ('C', 'A', 'B') -> الترتيب قد يختلف عندك لأن المجموعة غير مرتبة
print(tuple(f)) # ('A', 'B', 'C')

# List()

c = "Mohammed"                   # -> String
d = (1, 2, 3, 4, 5)              # -> Tuple
e = {"A", "B", "C"}              # -> set
f = {"A": 1, "B": 2, "C": 3}     # -> Dictionary

print(list(c)) # ['M', 'o', 'h', 'a', 'm', 'm', 'e', 'd']
print(list(d)) # [1, 2, 3, 4, 5]
print(list(e)) # ['A', 'C', 'B'] -> الترتيب قد يختلف عندك لأن المجموعة غير مرتبة
print(list(f)) # ['A', 'B', 'C']

# set()

c = "Mohammed"                   # -> String
d = (1, 2, 3, 4, 5)              # -> Tuple
e = ["A", "B", "C"]              # -> List
f = {"A": 1, "B": 2, "C": 3}     # -> Dictionary

print(set(c)) # {'o', 'e', 'h', 'd', 'a', 'M', 'm'}
print(set(d)) # {1, 2, 3, 4, 5}
print(set(e)) # {'B', 'C', 'A'}
print(set(f)) # {'B', 'C', 'A'}

# dict()

# c = "Mohammed"      (ERROR)    # -> String => Dictionary ما بنفع أحول النص ل 
# d = (1, 2, 3, 4, 5) (ERROR)    # -> Tuple => Tuple داخل Tuple ليش خطأ لأانو بدو مفتاح وقيمة , ممكن تزبط لو عملتها 
# e = ["A", "B", "C"] (ERROR)    # -> list =>  list داخل list عشان تزبط لازم أعمل Tupleنفس فكرة ال
# f = {"A", "B"}      (ERROR)    # -> set => ValueError , لأن كل عنصر لازم يكون زوج من مفتاح وقيمة
# ملاحظة: مجموعة فيها أزواج من نوع Tuple بتزبط
# dict({("A", 1), ("B", 2)}) => {'A': 1, 'B': 2} -> الترتيب قد يختلف

d = (("AA" , 1), ("BB", 2), ("CC", 3)) # -> Tuple Inside Tuple
e = [["AA" , 1], ["BB", 2], ["CC", 3]] # -> List Inside List

print(dict(d)) # {'AA': 1, 'BB': 2, 'CC': 3}
print(dict(e)) # {'AA': 1, 'BB': 2, 'CC': 3}
