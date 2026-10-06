# Lesson 077 - Modules Part 2 - Create Your Module
# Video: https://www.youtube.com/watch?v=tyOULB29Hs8

# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

# البحث داخل ملفات البايثون وطباعة المسارات وطريقة اضاف مسار جديد

# import sys
# sys.path.append(r"C:\MyModules") # إضافة مجلد جديد يبحث فيه بايثون عن المديولات
# print(sys.path) 

# ------------------------------------------------------------

import AlBashaModules

print(dir(AlBashaModules))

# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sayHello', 'sayHowAreYou']

AlBashaModules.sayHello("Mohammed") # Hello Mohammed
AlBashaModules.sayHello("Galeb") # Hello Galeb
AlBashaModules.sayHello("Emad") # Hello Emad

AlBashaModules.sayHowAreYou("Mohammed") # How Are You Mohammed
AlBashaModules.sayHowAreYou("Galeb") # How Are You Galeb

# ------------------------------------------------------------

import AlBashaModules as AM # للمديول الخاص بي (Alias Name)هيك انا بعمل اسم مستعار

AM.sayHello("Kaled") # Hello Kaled

# ------------------------------------------------------------

from AlBashaModules import sayHello

sayHello("Osama") # Hello Osama

from AlBashaModules import sayHello as ss # الي داخل المديول functionهيك انا بعمل اسم مستعار لل

ss("Ahmed") # Hello Ahmed
