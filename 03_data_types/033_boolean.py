# Lesson 033 - Boolean
# Video: https://www.youtube.com/watch?v=eDmGoHk1Y8k

# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need To Know If Your Code Output Is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace()) # True

print(100 > 200) # False

print(100 > 90) # True

# True Values

print(bool("Osama"))         # True
print(bool(100))             # True
print(bool(True))            # True
print(bool([1, 2, 3, 4]))    # True

# False Values

print(bool(""))      # False
print(bool(''))      # False
print(bool(0))       # False
print(bool(False))   # False
print(bool([]))      # False
print(bool(()))      # False
print(bool({}))      # False
print(bool(None))    # False


