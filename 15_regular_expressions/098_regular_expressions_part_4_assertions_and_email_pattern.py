# Lesson 098 - Regular Expressions Part 4 Assertions & Email Pattern
# Video: https://www.youtube.com/watch?v=bxssGTLjktA

# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
# -------------------------

# مثال للتجربة: نفحص قائمة إيميلات بالنمط السابق

import re

emails = ["user@example.com", "user.name@site.org", "user@site", "user@example.co"]

for email in emails:

    if re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$", email):
        print(f"{email} => Valid")
    else:
        print(f"{email} => Not Valid")

# user@example.com => Valid
# user.name@site.org => Valid
# user@site => Not Valid
# user@example.co => Not Valid

# العلامة ^ تعني أن الماتش يبدأ من أول النص، والعلامة $ تعني أنه ينتهي عند آخره
# بدونهما يقبل النمط إيميلا موجودا في وسط نص طويل

# ملاحظة مهمة: المجال A-z يشمل أيضا رموزا تقع بين Z و a في جدول الرموز
print(re.findall("[A-z]", "A_Z^a")) # ['A', '_', 'Z', '^', 'a']
# لذلك الأدق أن نكتب المجال هكذا
# [A-Za-z]
