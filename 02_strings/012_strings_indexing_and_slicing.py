# Lesson 012 - Strings - Indexing And Slicing
# Video: https://www.youtube.com/watch?v=PEp4oqzthnw

# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"
print(myString[0]) # Index 0 => I (يطبع أول حرف من الجملة من الأول ويبدأ من (0
print(myString[5]) # Index 5 => e يطبع الحرف السادس من الجملة لأن العد يبدأ من صفر

print(myString[-1]) # Index -1 => n يطبع الحرف الأول من الآخر ويبدأ العد من (-1)
print(myString[-6]) # Index -6 => P يطبع الحرف السادس من الجملة من الآخر 

# Slicing (Access Multiple sequence Items) بيأخذ قطعة من الجملة
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[4:9]) # ve Py 
print(myString[3:5]) # ov
print(myString[:10]) # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:]) # If End Is Not Here Will Go To The End (e Python)
print(myString[:]) # Full Data

print(myString[0::1]) # I Love Python (Steps By Default 1)
print(myString[::1]) # I Love Python
print(myString[::2]) # ILv yhn (بطبع حرف وبفشق حرف)
print(myString[::3]) # Io tn (بطبع حرف وبفشق حرفين)

