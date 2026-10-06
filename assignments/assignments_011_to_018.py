# Assignment 01

Name = "Mohammed"
Age = 22
Country = "Gaza"

print(f"\"Hello \'{Name}\', How You Doing \\ \"\"\" My Age Is \"{Age}\"\" + And Your Country Is: {Country}")
# "Hello 'Mohammed', How You Doing \ """ My Age Is "22"" + And Your Country Is: Gaza
# _______________________________________________________________________________________________________

# Assignment 02

print(f"\"Hello \'{Name}\', How You Doing \\ \n\"\"\" My Age Is \"{Age}\"\" + \nAnd Your Country Is: {Country}")
# "Hello 'Mohammed', How You Doing \ 
# """ My Age Is "22"" + 
#  And Your Country Is: Gaza
# _______________________________________________________________________________________________________

# Assignment 03

name = 'Elzero'

print(f'Second Letter Is "{name[1]}" \nThird Letter Is "{name[2]}" \nLast Letter Is "{name[-1]}"')
print(name[1:4])
print(name[::2])
print(name[-2::-2])

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
# "lze"
# "Ezr"
# "rzE"
# _______________________________________________________________________________________________________

# Assignment 04

name = "#@#@Elzero#@#@"

print(name.strip("#@"))

# Elzero
# _______________________________________________________________________________________________________

# Assignment 05

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

# 0009
# 0015
# 0130
# 0950
# 1500
# _______________________________________________________________________________________________________

# Assignment 06

name_one = "Mohammed"
name_two = "Mohammed_AlBasha"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

# @@@@@@@@@@@@Mohammed
# @@@@Mohammed_AlBasha
# _______________________________________________________________________________________________________

# Assignment 07

name_one = "MoHaMmEd"
name_two = "mOhAmMeD"

print(name_one.swapcase())
print(name_two.swapcase())

# mOhAmMeD
# MoHaMmEd
# _______________________________________________________________________________________________________

# Assignment 08

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love")) # 2
# _______________________________________________________________________________________________________

# Assignment 09

name = "Elzero"

print(name.index("z")) # 2
# _______________________________________________________________________________________________________

# Assignment 10,11

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))
print(msg.replace("<3", "Love"))

# I Love Python And Although <3 Elzero Web School
# I Love Python And Although Love Elzero Web School
# _______________________________________________________________________________________________________

# Assignment 12

Name = "Mohammed"
Age = 22
Country = "Gaza"

print("Hello %s, And My Age Is %.1f, And My Country Is: %s" %(Name,Age,Country))        # الطريقة القديمة
print("Hello {}, And My Age Is {:.1f}, And My Country Is: {}".format(Name,Age,Country)) # الطريقة الحديثة
print(f"Hello {Name}, And My Age Is {Age:.1f}, And My Country Is: {Country}")           # الطريقة الأحدث

# Hello Mohammed, And My Age Is 22.0, And My Country Is: Gaza
