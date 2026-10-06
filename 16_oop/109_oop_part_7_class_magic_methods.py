# Lesson 109 - OOP Part 7 - Magic Methods
# Video: https://www.youtube.com/watch?v=dz78-WPduag

# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class Skill:

    def __init__(self):

        self.skills = ["Html", "Css", "Js"]

    def __str__(self):
        
        return f"This Is My Skills => {self.skills}"

    def __len__(self):
        
        return len(self.skills)



profile = Skill()

print(profile.__class__) # <class '__main__.Skill'>

# ----------------------------

# قبل إضافة الميثود __str__ كان ناتج الطباعة عنوان الكائن في الذاكرة فقط
# <__main__.Skill object at 0x7acd51ffe6c0>

# بعد إضافة الميثود __str__ أصبح الناتج هكذا

print(profile) # This Is My Skills => ['Html', 'Css', 'Js']

# فقط عملناها لتوضيح __str__ وفي العادة ما بنستخدم 

# ----------------------------

# قبل إضافة الميثود __len__ كان استخدام len مع الكائن يعطي خطأ
# TypeError: object of type 'Skill' has no len()

# بعد إضافة الميثود __len__ أصبح الناتج هكذا

print(len(profile)) # 3

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile)) # 5   => len لاحظ بعد ما اضفنا عناصر زاد طول ال

# ----------------------------

# my_string = "Mohammed" # -> str من الكلاس Constructor او Instance عبارة عن 

# print(type(my_string)) # <class 'str'>

# print(my_string.__class__) # <class 'str'>

# print(my_string.upper()) # MOHAMMED

# .... السابق هي نفس الطريقة التاليه ولكن خلف الكواليس

# print(str.upper(my_string)) # MOHAMMED

# print(dir(str))

# -----------------------------------------

