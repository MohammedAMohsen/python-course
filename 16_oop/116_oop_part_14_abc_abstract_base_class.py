# Lesson 116 - OOP Part 14 ABCs Abstract Base Class
# Video: https://www.youtube.com/watch?v=bRHRoB28sxk

# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @abstractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

# class Programming:

#     def has_oop(self): # -> يعني المفترض هاد الكلاس يكون كلاس مجرد وعام 
#         return "Yes" # -> غير منطقي انو هادي الميثود في كلاس البرمجة بشكل عام
#         # -> من غير المنطقي اجاوب اه او لا هاد السؤال بكون للغة نفسها زي بايثون جافا بسكال ,OOPهل البرمجة بتعدم ال

from abc import ABCMeta, abstractmethod

# طريقة أقصر تعطي نفس النتيجة
# from abc import ABC
# class Programming(ABC):

class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):

        pass
    
    @abstractmethod
    def has_name(self):

        pass

    def anything(self): # -> Abstract مش من الضروري اضيفو في باقي الكلاسات لانو مش 

        pass

class Python(Programming):
      
    def has_oop(self):

        return "Yes"

    def has_name(self):

        return "Python"


class Pascal(Programming):
      
    def has_oop(self):

        return "No"
    
    def has_name(self):

        return "Pascal"
      

# one = Programming()

# print(one.has_oop()) # Yes

# -----------------------------------------------------

# Abstract بعد ما عملنا الكلاس والميثود الي داخل الكلاس 

# one = Programming() # Error
# TypeError: Can't instantiate abstract class Programming without an implementation for abstract methods 'has_name', 'has_oop'
# لا يمكن إنشاء كائن من الكلاس المجرد نفسه، هو فقط قالب للكلاسات التي ترث منه

two = Python()
three = Pascal()

print(two.has_oop()) # Yes

print(three.has_oop()) # No

# -----------------------------------------------------
# has_name()سناريو بعد اضافة الميثود ال
# -----------------------------------------------------

# has_name() باسم Abstract Class لاحظ معي وجود ميثود اخرى في الكلاس الرئيسي الي هو عبارة عن 
# بدون مشاكل has_oop()هتلاحظ في استدعاء كلاس البايثون وباسكال ل @abstractmethod هاد الميثود مش معمول الها 
# في باقي الكلاسات (بايثون وباسكال) الي بتورث من الكلاس الرئيسي has_name()حتى ولو مش موجود ميثود ال

# Abstractفهنا من الضروري اضافة هذا الميثود في الكلاسات التي ترث من الكلاس ال @abstractmethod <- has_name()اما في حال اصبح ال
# عبارة عن امبليمنت لازم ينعمل الو صورة لكل الكلاسات التي بترث منه AbstractMethodو ال AbstractClassلانه بالمختصر الشديد ال
# Abstractفي كل الكلاسات الي بترث من الكلاس الرئيسي ال Overrideلازم اعمل للميثود نفسها @abstractmethod عبارة عن has_name()يعني في حال اصبح الميثود
# Mainفي ال (instantiate) حتى لو انا ما بعمللها استدعاء 

# -----------------------------------------------------

four = Python()
five = Pascal()

# لو لم نضف الميثود has_name() داخل الكلاسين، لظهر هذا الخطأ عند إنشاء الكائن نفسه
# TypeError: Can't instantiate abstract class Python without an implementation for abstract method 'has_name'
# TypeError: Can't instantiate abstract class Pascal without an implementation for abstract method 'has_name'

# داخل كلاس بايثون وكلاس باسكال has_name()لميثود ال Override بعد ما اعملت 

print(four.has_oop()) # Yes

print(five.has_oop()) # No

# -----------------------------------------------------
# Abstract دخل الكلاس الي بكون @abstractmethod الميثود الي بتكون معمول الها 
# Abstract لازم اضيف نفس المثود هادي في جميع الكلاسات الي بتورث من الكلاس الي معمول الو 
# داخل البرنامج عندي instantiate حتى لو انا ما بستدعي هادي الميثود او بعمل الها
# -----------------------------------------------------
