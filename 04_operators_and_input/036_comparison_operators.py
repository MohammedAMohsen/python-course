# Lesson 036 - Comparison Operators
# Video: https://www.youtube.com/watch?v=bBxO141Jq6I

# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------

# Equal + Not Equal

print(100 == 100) # True
print(100 == 200) # False
print(100 == 100.00) # True
print(100 == 40) # False

print(100 != 100) # False
print(100 != 200) # True
print(100 != 100.00) # False
print(100 != 40) # True

# Greater Than + Less Than

print(100 > 100) # False
print(100 > 200) # False
print(100 > 100.00) # False
print(100 > 40) # True

print(100 < 100) # False
print(100 < 200) # True
print(100 < 100.00) # False
print(100 < 40) # False

# Greater Than Or Equal + Less Than Or Equal

print(100 >= 100) # True
print(100 >= 200) # False
print(100 >= 100.00) # True
print(100 >= 40) # True

print(100 <= 100) # True
print(100 <= 200) # True
print(100 <= 100.00) # True
print(100 <= 40) # False
