# Lesson 026 - Set
# Video: https://www.youtube.com/watch?v=PSc6QX4Py7k

# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# ---- Not Ordered And Not Indexed ----

mySetOne = {"Ahmed","Mohammed",100}

print(mySetOne) # {'Mohammed', 100, 'Ahmed'} -> بتطبع بترتيب عشوائي
# print(mySetOne[0]) Error -> ما بتقدر تصل لعنصر معين بعينه

# ---- Slicing Cant Be Done ----

myTuple = (1, 2, 3, 4, 5)
print(myTuple[0:3]) # (1, 2, 3) 

mySetTwo = {1, 2, 3, 4, 5}
# print(mySetTwo[0:3])  Error  -> set object is not subscriptable

# ---- Has Only Immutable Data Types , Only (Numbers, Strings, Tuples) ----

# mySetThree = {"Mohammed", 100, 13.4, True, [1, 2, 3]} # unhashable type: 'list'
# print(mySetThree) Error -> Setما بنفع أضيف قائمة داخل ال 

mySetfour = {"Mohammed", 100, 13.4, True, (1, 2, 3)}
print(mySetfour) # {True, 100, 'Mohammed', (1, 2, 3), 13.4} -> Setداخل ال Tuple بنفع أضيف

# ---- Items Is Unique ----

mySetfive = {1, 2, "Mohammed", "One", 1, 40, "One"}
print(mySetfive) # {'One', 1, 2, 40, 'Mohammed'} -> لاحظ أنو ما بطبع العناصر المكررة, يعني بلغيها
