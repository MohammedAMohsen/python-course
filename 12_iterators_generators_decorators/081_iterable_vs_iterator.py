# Lesson 081 - Iterable Vs Iterator
# Video: https://www.youtube.com/watch?v=MwBk42xwjjA

# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

# is Iterable:

myString = "Mohmmed"

myList = [1,2,4,5,6,7]

for letter in myString:
    print(letter, end=" ") # M o h m m e d

print("")

for list in myList:
    print(list, end=" ") # 1 2 4 5 6 7 

print("")

# ------------------------------------

# is Not Iterable:

# myNumber = 10
# myNumber = 10.34
# mybool = false

# for n in myNumber:
#     print(n)  # => TypeError: 'int' object is not iterable

# ------------------------------------

# Create Iterator:

myString = "Mohmmed"

# print(next(myString)) => TypeError: 'str' object is not an iterator

myIterator = iter(myString)

print(next(myIterator)) # M
print(next(myIterator)) # o
print(next(myIterator)) # h
# .
# .
# .

# بشكل افتراضي Iter هي بتعمل for

# for litter in "Mohammed":
#     print(litter)

# :الفور الأولى هي نفسها الفور الثانية ولكن بتعملها اللغة خلف الكواليس كالتالي

# for litter in iter("Mohammed"):
#     print(litter)

