# Lesson 102 - Regular Expressions Part 8 Group Training's & Flags
# Video: https://www.youtube.com/watch?v=MLb7pPOEJlg

# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group()) # https://www.elzero.org:8080/category.php?article=105?name=how-to-do

print(search.group(1)) # https

print(search.group(5)) # 8080

# ------------------------------------------------

print(search.groups()) # ('https', 'www', 'elzero', 'org', '8080', 'category.php?article=105?name=how-to-do')

for group in search.groups():

    print(group)

# Output:

# https
# www
# elzero
# org
# 8080
# category.php?article=105?name=how-to-do

# ------------------------------------------------

# local = ["Protocol", "Sub Domain", "Domain Name", "Top Level Domain", "Port", "Query"]
# i = 1
# for web in local:
#     print(f"{web}: {search.group(i)}")
#     i += 1

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query: {search.group(6)}")

# Output:

# Protocol: https
# Sub Domain: www
# Domain Name: elzero
# Top Level Domain: org
# Port: 8080
# Query: category.php?article=105?name=how-to-do

# ------------------------------------------------

# مثل تجاهل الأسطر تجاهل حساسية الأحرف وهكذا regularبقدر اضيف الخواص الي بتيجي مع ال

# الخواص تكتب كقيمة واحدة، ونجمع أكثر من خاصية بالعلامة |
# re.IGNORECASE => تجاهل حالة الأحرف
# re.MULTILINE  => العلامتان ^ و $ تعملان على كل سطر وحده
# re.DOTALL     => النقطة تطابق السطر الجديد أيضا
# re.VERBOSE    => تسمح بكتابة النمط على عدة أسطر مع تعليقات

search = re.search(r"^[a-z]+$", "MOHAMMED\nmohsen")
print(search) # None -> بدون خواص النمط يحتاج النص كله أحرفا صغيرة وفي سطر واحد

search = re.search(r"^[a-z]+$", "MOHAMMED\nmohsen", re.IGNORECASE | re.MULTILINE)
print(search.group()) # MOHAMMED

print(re.findall(r"^[a-z]+$", "MOHAMMED\nmohsen", re.IGNORECASE | re.MULTILINE)) # ['MOHAMMED', 'mohsen']
