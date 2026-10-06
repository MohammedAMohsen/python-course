# Assignment 01

import re

for m in re.findall(r'\w ', "eeeeA llllLl lllzzZzzzb bnana eros operationh polla "):
    print(m)

# Output: أخر حرف من كلمة بحيث تم عمل ماتش لكل حرف بعدة مسافة

# A 
# l 
# b 
# a
# s 
# h 
# a 

# _______________________________________________________________________________________________________
# Assignment 02

search = re.search(r"(?<=L)[A-z]+", "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111")

print(search.group()) # Elzero

# ولكن لا يظهر بالناتج L بدون الأرقام والشرط هنا ان يكون قبلها حرف ال Elzeroاعمل ماتش لكلمة ال

# _______________________________________________________________________________________________________
# Assignment 03

my_phone = """
+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01000000000
0100 600 1234
(0100) 600-1
(0100) 600-12
"""

for m in re.findall(r"\+?\(\d{4}\)\s\d{2,4}-\d{4}", my_phone):
    print(m)

# Output: بما يطابق اول ثلاث ارقام جوالات Regular Expression اعمل 

# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234

# _______________________________________________________________________________________________________
# Assignment 04

# ===============================
# (...)	Capturing group
# ===============================

# Match في نتائج ال Groupتُستخدم لتجميع جزء من النمط وتظهر كـ Regular Expression الأقواس () في
# مثل المثال الي في الدرس 102 واستفدنا من القروب في الناتج انو اقدرنا نقطع الرابط

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.groups()) # ('https', 'www', 'elzero', 'org', '8080', 'category.php?article=105?name=how-to-do')

# =============================== ----------------------
# (?:...)	Non-capturing group   - هذا هو سؤال الواجب -
# =============================== ----------------------

# في النتائج Group تستخدم لتجيمع النمط فقط بدون انشاء Non-capturing group (?:...) اما

my_link = """
http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net
"""

for f in re.findall(r"https?://(?:www\.)?\w+\.(?:org|com)+(?::\d+)?/\w+\.\w+", my_link):
    print(f)

# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py