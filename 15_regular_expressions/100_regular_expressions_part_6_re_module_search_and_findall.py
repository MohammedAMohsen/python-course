# Lesson 100 - Regular Expressions Part 6 Re Module Search & FindAll
# Video: https://www.youtube.com/watch?v=UKA-3O7XwPs

# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

# =======================================
#            search()
# =======================================

import re

my_search = re.search("[A-Z]", "MohammedAlbasha")

print(my_search) # <re.Match object; span=(0, 1), match='M'>

# فيه اول عنصر عمل فيه ماتش وموقع بالجملة Object اعطاني

# ---------------------------------------

print(my_search.span()) # (0, 1)

print(my_search.string) # MohammedAlbasha

print(my_search.group()) # M

# ---------------------------------------

my_search2 = re.search("[A-Z]", "MMohsen")

print(my_search2.group()) # M

# ---------------------------------------

my_search3 = re.search(r"[A-Z]{2}", "MMhsenEErome")

print(my_search3.group()) # MM

# ---------------------------------------

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "user@example.com")

if is_email:

    print("This Is A Valid Email :)")
    print(is_email.span())
    print(is_email.string)
    print(is_email.group()) 

else:

    print("This Is Not A Valid Email :(")
    
# Output:

# This Is A Valid Email :)
# (0, 16)
# user@example.com
# user@example.com

# =======================================
#            findall()
# =======================================

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

# انتبه: العلامة | هنا تفصل النمط كله إلى قسمين
# يعني إما إيميل ينتهي بـ .com أو كلمة net وحدها في أي مكان
# الأصح وضع الخيارات داخل قوسين، والعلامة ?: تمنع findall من إرجاع ما داخل القوس فقط
# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.(?:com|net)", email_input)

empty_list = []

# بفحص الناتج اذا عمل ماتش بيعطي الماتش الناتج واذا ما عمل ماتش برجع قائمة فارغة findall ليش فحصت بقائمة فارغة , عشان ال

if search != []:

    empty_list.append(search)

    print("Email Added :)")
    
else:
    print("Invalid Email")


for email in empty_list:
    
    print(email)
