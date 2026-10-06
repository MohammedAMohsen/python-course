# Lesson 113 - OOP Part 11 -  Encapsulation
# Video: https://www.youtube.com/watch?v=_zJ1nQto7Mw

# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attributes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Or Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------


class Member:

    def __init__(self, name):
        
         self.name = name # Public


one = Member("Mohammed")
 
print(one.name) # Mohammed

one.name = "Osama"

print(one.name) # Osama

# قدرت اعدل على الأسم بسهولة Public عبارة عن nameلاحظ عشان ال

# -------------------------------------------------

class MemberTwo:

    def __init__(self, name):
        
         self._name = name # Protected


one = MemberTwo("Mohammed")
 
print(one._name) # Mohammed

one._name = "Osama"

print(one._name) # Osama

# ---------------------------------------------------

class MemberThree:

    def __init__(self, name):
        
         self.__name = name # Private
    
    def say_hello(self):
         
         return f"Hello {self.__name}"
    

one = MemberThree("Mohammed")

# print(one.__name) # AttributeError

# ما بقدر اصل الها خارج الكلاس ولا بقدر اعدل عليها <- Private 

# لكن بقدر اصل واعدل عليها داخل الكلاس نفسو

print(one.say_hello()) # Hello Mohammed

# ---------------------------------------------------

# (لكن للأسف اللغة ما بدعم هذة الخواص السابقة بطريقة فعالة, ممكن بطريقة احتيالية اوصل للعناصر الخاصة والمحمية)

print(one._MemberThree__name) # Mohammed
