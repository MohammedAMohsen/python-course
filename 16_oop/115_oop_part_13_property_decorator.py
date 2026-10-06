# Lesson 115 - OOP Part 13 @Property Decorator
# Video: https://www.youtube.com/watch?v=UgpyNxNiPRg

# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class Member:

    def __init__(self, name, age):
        
        self.name = name

        self.age = age

    def say_hello(self):

        return f"Hello {self.name}"
    
    def age_in_days(self):

        return self.age * 365
    
    @property
    def age_in_days_pro(self):

        return self.age * 365
    

one = Member("Mohammed", 23)

print(one.name) # Mohammed
print(one.age) # 23
print(one.say_hello()) # Hello Mohammed

print(one.age_in_days()) # 8395

# بدون أقواس يطبع الميثود نفسها وليس ناتجها (والعنوان يختلف في كل تشغيل)
print(one.age_in_days) # <bound method Member.age_in_days of <__main__.Member object at 0x74c1a8702db0>>

print(one.age_in_days_pro) # 8395

# print(one.age_in_days_pro()) # TypeError: 'int' object is not callable
# الميثود التي عليها @property نستخدمها مثل المتغير بدون أقواس
# لأن ناتجها رقم، والرقم لا يمكن استدعاؤه بالأقواس


