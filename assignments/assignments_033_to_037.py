# Assignment 01

print(bool("Mohammed"))   # True
print(bool(100))          # True
print(bool(True))         # True
print(bool([1, 2, 3, 4])) # True

print(bool(""))     # False
print(bool(0))      # False
print(bool(False))  # False
print(bool([]))     # False
# _______________________________________________________________________________________________________
# Assignment 02

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50) # True
# _______________________________________________________________________________________________________
# Assignment 03

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two) # True
print(num > num_one and num > num_two) # False
# _______________________________________________________________________________________________________
# Assignment 04

num_one = 10
num_two = 20

result = num_one + num_two

print(result) # 30
print(result**3) # 27000
print((result**3)%26000) # 1000
print(((result**3)%26000)/5) # 200.0
print(type(str(((result**3)%26000)/5))) # <class 'str'>