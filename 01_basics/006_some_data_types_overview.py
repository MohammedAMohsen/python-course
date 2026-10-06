# Lesson 006 - Some Data Types Overview
# Video: https://www.youtube.com/watch?v=43lT7k0Zws0

# ----------------------------
# type() بتظهر نوع البيانات الي بتعامل معاها
# All Data in Python is Object  
# ----------------------------

print(type(10))   # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))     # float => Floating Point Number
print(type(1.934324))  # float => Floating Point Number
print(type(-10.9244))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1,2,3,4,5]))  # list => list

print(type((1,2,3,4,5)))  # tuple => Tuple  listقريبة من ال

print(type({ "One" : 1, "Two" : 2, "Three": 3}))  # dict => Dictionary { "Key" : val }

print(type(True))    # bool => Boolean
print(type(False))   # bool => Boolean
print(type(2 == 2))  # bool => Boolean
