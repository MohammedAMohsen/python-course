# Lesson 096 - Regular Expressions Part 2 Quantifiers
# Video: https://www.youtube.com/watch?v=3B8qYBBml68

# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2,5}	Between 2 and 5
# {2,}	2 or more
# {,5}	Up to 5
# -------------

import re

my_text = """
A
ABC
123 123 1234
ABCD ABCDEF
A B C D E F
"""

my_search = re.findall(r"A\w", my_text) # وراه اي حرف آخر A أي حرف  

print(my_search) # ['AB', 'AB', 'AB']

my_search = re.findall(r"A\w\w", my_text) # وراه اي حرفين A أي حرف

print(my_search) # ['ABC', 'ABC', 'ABC']

my_search = re.findall(r"A\w\w\w\w", my_text) # وراه اي 4 حروف A أي حرف

print(my_search) # ['ABCDE']

my_search = re.findall(r"\sD", my_text) # قبلو مسافة Dحرف ال

print(my_search) # [' D'] -> المسافة جزء من الماتش

my_search = re.findall(r"\w{4}", my_text) # ماتش مع اربع احرف او اربع ارقام

print(my_search) # ['1234', 'ABCD', 'ABCD']

my_search = re.findall(r"\w{5,7}", my_text) # ماتش مع اي احرف او أرقام مكونة من 5 الى 7

print(my_search) # ['ABCDEF']

# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2,5}	Between 2 and 5
# {2,}	2 or more
# {,5}	Up to 5

Phone = """
001 5456-820
Hello Mohammed
123 123 1234
ABCD ABCDEF
"""

my_search = re.findall(r"\d{3}\s\d{4}-\d{3}", Phone) 

print(my_search) # ['001 5456-820']
