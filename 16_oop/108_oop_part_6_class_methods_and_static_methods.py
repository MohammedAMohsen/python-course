# Lesson 108 - OOP Part 6 - Class Methods And Static Methods
# Video: https://www.youtube.com/watch?v=GQVGcJblo6U

# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Doesn't Need self Or cls (It Can Still Take Normal Parameters)
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member:

    not_allowed_name = ["Hell", "Shitt", "Baloot"]

    user_num = 0

    @classmethod
    def show_user_count(cls): # Class Methods حتى تعمل ال Parameter cls ضروري انضيف ال

        print(f"We Have {cls.user_num} User In Our System")


    @staticmethod 
    def say_hello(): # Parameter ليس من الضروري ان انضيف اي staticmethodال
        
        print("Hello From Static Method")


    def __init__(self, first_name, middle_name, last_name, gender): # Instance Methodsحتى تعمل ال Parameter selfضروري انضيف ال
        
        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender 

        Member.user_num += 1

    def full_name(self):
        
        if self.fname in Member.not_allowed_name:

            raise ValueError("Name Not Allowed")
        
        else:

            return f"{self.fname} {self.mname} {self.lname}"

  
    def name_with_title(self):

        if self.gender == "Male":

            return f"Hello Mr.{self.fname}"
        
        elif self.gender == "Female":

            return f"Hello Miss.{self.fname}"

        else:

            return f"{self.fname}"


    def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

    
    def delete_user(self):

        Member.user_num -= 1  # -> كل استدعاء للهذه الأنستنت ميثود بنقص عدد المستخدمين الي عندي

        return f"User {self.fname} Is Deleted :("
    

member_one = Member("Mohammed", "Alaa", "Mohsen", "Male")
member_two = Member("Mona", "Boime", "Jamal", "Female")
member_three = Member("Karrem", "Abd", "Fiez", "Male")
member_four = Member("Hell", "Fal", "Gone", "Female")

# Class Attributes هاد خاصة بال
print(Member.user_num)

# Class Methods هاد خاصة بال
Member.show_user_count() # We Have 4 User In Our System

# ----------------------

print(member_one.full_name())       # Mohammed Alaa Mohsen
print(Member.full_name(member_one)) # Mohammed Alaa Mohsen
# السطر الثاني هو نفس السطر الأول، وهكذا تنفذه اللغة في الخلفية
# فالكائن member_one يرسل نفسه تلقائيا كقيمة للمعامل self

# ----------------------

Member.say_hello() # Hello From Static Method
