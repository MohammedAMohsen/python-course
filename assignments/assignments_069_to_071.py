# Assignment 01

values = (0, 1, 2)

if any(values): # True

    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#                                         my_var = 0

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
#      True         or     False        or     False   =  True

    print("Good")

else:

    print("Bad")

# (Good الإجابة التي ستظهر بعد التشغيل هي)

# _______________________________________________________________________________________________________
# Assignment 02

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# _______________________________________________________________________________________________________
# Assignment 03

n = 20 
# n =  21
# n = 22

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")

# _______________________________________________________________________________________________________
# Assignment 04

def my_all(iterable):
    re = "True" # قيمة ابتدائية حتى لا يظهر خطأ لو كانت القائمة فارغة
    for elemint in iterable:
        if bool(elemint) != False:
            re = "True"
        else:
            re = "False"
            break
    return re

print(my_all([1, 2, 4]))# True
print(my_all([1, 2, 3, []])) # False

# -------------------------------------------------------------

def my_any(iterable):
    re = "False" # قيمة ابتدائية حتى لا يظهر خطأ لو كانت القائمة فارغة
    for elemint in iterable:
        if bool(elemint) != False:
            re = "True"
            break
        else:
            re = "False"
    return re

print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# -------------------------------------------------------------    

def my_min(iterable):

    if iterable != [] and iterable != 0 and iterable != ():
        min = iterable[0]
        for num in iterable:
            if num < min:
                min = num
    else:
        return "The Empty Input :("
    
    return(f"The Smallest Number Is: {min}")      


print(my_min([15, 10, 4, 17, 12, -10, -6, 13, -9])) # -10
print(my_min([10, 100, -20, -100, 50, -50, -10, -9]))# -100
print(my_min([]))# The Empty Input :(

# -------------------------------------------------------------

def my_max(iterable):

    if iterable != [] and iterable != 0 and iterable != ():
        max = iterable[0]
        for num in iterable:
            if num > max: 
                max = num
    else:
        return "The Empty Input :("
    
    return(f"The Largest Number Is: {max}")

print(my_max([15, 10, 4, 17, 12, -10, -6, 13, -9])) # 17
print(my_max([10, 100, -20, -100, 50, -50, -10, -9]))# 100
print(my_max([]))# The Empty Input :(