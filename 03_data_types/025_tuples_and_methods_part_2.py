# Lesson 025 - Tuples And Methods Part Two
# Video: https://www.youtube.com/watch?v=MDR7c5ozo7I

# -----------
# -- Tuple --
# -----------

# Tuple With One Element

myTuple1 = ("Mohammed")
myTuple2 = "Mohammed"

print(type(myTuple1)) # <class 'str'>
print(type(myTuple2)) # <class 'str'>

# (,) لازم أضيف العلامة Tuple عشان أعرّف أنهم من نوع

myTuple3 = ("Mohammed",)
myTuple4 = "Mohammed",

print(type(myTuple3)) # <class 'tuple'>
print(type(myTuple4)) # <class 'tuple'>

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6, 7)
dd = (2,3)

c = a + b
d = a + ('A', 'B', True) + b
dd += (4,5) 

print(c) # (1, 2, 3, 4, 5, 6, 7)
print(d) # (1, 2, 3, 4, 'A', 'B', True, 5, 6, 7)
print(dd) # (2, 3, 4, 5)

# Tuple, List, String Repeat (*) -> بكرر بالمقدار المحدد

myString = "Mohammed "
myList = [1, 2]
myTuple5 = ('A', 'B')

print(myString * 5) # Mohammed Mohammed Mohammed Mohammed Mohammed
print(myList * 5)   # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple5 * 5) # ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')

# Methods => count()

e = (1, 8, 3, 8, 5, 6, 7, 8)
print(e.count(8)) # 3

# Methods => index()

f = (1, 3, 7, 8, 2, 6, 5)
print(f"The Position Of Index Is: {f.index(7)}") # The Position Of Index Is: 2

# Tuple Destruct

g = ('A', 'B', 'C')

x, y, z = 'a', 'b', 'c'

# على المتغيرات الي عندي بشرط أن يكون عدد المتغيرات يساوي عدد العناصرTupleلو أنا حابب أوزع عناصر ال 
x, y, z = g

print(x, y, z) # A B C

#  (_) لو أنا عندي عنصر مش حابب أضيفو وأعملو متغير , بسيب مكانو 

h = ('A', 4, 'B', 'C')

r, _, t, s = h

print(r, t, s) # A B C
