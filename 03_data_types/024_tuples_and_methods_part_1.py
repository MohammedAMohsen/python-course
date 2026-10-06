# Lesson 024 - Tuples And Methods Part One
# Video: https://www.youtube.com/watch?v=gwKxpFG_h_8

# -----------------------------
# -- Tuple -------------------- 
# -----------------------------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Mohammed", "Ahmed") 
myAwesomeTupleTwo = "Mohammed", "Ahmed"

print(myAwesomeTupleOne) # ('Mohammed', 'Ahmed')
print(myAwesomeTupleTwo) # ('Mohammed', 'Ahmed')

print(type(myAwesomeTupleOne)) # <class 'tuple'>
print(type(myAwesomeTupleTwo)) # <class 'tuple'>

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)

print(myAwesomeTupleThree[0])  # 1
print(myAwesomeTupleThree[-1]) # 5

# Tuple Assign Values -> ما بتسمح بإعادة تعيين للقيم أو التعديل
# myAwesomeTupleThree[2] = "Three" <-- Error --> 'tuple' object does not support item assignment

# Tuple Items

myAwesomeTupleFive = ("Mohammed", "Mohammed", 1, 2, 3, 100.5, True)

print(myAwesomeTupleFive[1])  # Mohammed
print(myAwesomeTupleFive[-1]) # True
