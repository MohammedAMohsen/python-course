# Assignment 01

Name =  "Mohammed",

print(Name)       # ('Mohammed',)
print(type(Name)) # <class 'tuple'>
# _______________________________________________________________________________________________________
# Assignment 02

friends = ("Osama", "Ahmed", "Sayed")

frintdsEdit = list(friends)
frintdsEdit[0] = "Elzero"
friends = tuple(frintdsEdit)

print(friends)       # ('Elzero', 'Ahmed', 'Sayed')
print(type(friends)) # <class 'tuple'>
print(f"{len(friends)} Elements") # 3 Elements
# _______________________________________________________________________________________________________
# Assignment 03

nums = (1, 2, 3)
letters = ("A", "B", "C")

NumLetter = nums + letters

print(NumLetter)      # (1, 2, 3, 'A', 'B', 'C')
print(f"{len(NumLetter)} Elements") # 6 Elements
# _______________________________________________________________________________________________________
# Assignment 04

my_tuple = (1, 2, 3, 4)

a, b, _, c = my_tuple

print(a) # 1
print(b) # 2
print(c) # 4