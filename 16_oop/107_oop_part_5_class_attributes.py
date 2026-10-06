# Lesson 107 - OOP Part 5 - Class Attributes
# Video: https://www.youtube.com/watch?v=48OyTbNlveE

# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class Member:

    not_allowed_name = ["Hell", "Shitt", "Baloot"]

    user_num = 0

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender 

        Member.user_num += 1  # -> للكلاس زود عدد المستخدمين Instance Methodsكل ما اضيف مستخدم عبر استدعاء ال

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
    


# print(dir(Member))
# مش بالميثود الخاصة بالكلاس Instanceيعرض الميثود العامة والميثود الي أنشأنها الخاصة بال
# وهتلاحظ وجود آتريبيوت خاصة بالكلاس فقط التي تكون معرفة خارج الكونستركتر كمثود للكلاس
# [...., 'full_name', 'get_all_info', 'name_with_title', 'not_allowed_name', 'user_num']


print(Member.user_num) # 0 -> كان عدد المستخدمين صفر Member من الكلاس (Objects) Instance Methods قبل ما أنشاء 

member_one = Member("Mohammed", "Alaa", "Mohsen", "Male")
member_two = Member("Mona", "Boime", "Jamal", "Female")
member_three = Member("Karrem", "Abd", "Fiez", "Male")
member_four = Member("Hell", "Fal", "Gone", "Female")

# print(member_one.get_all_info()) # Hello Mr.Mohammed, Your Full Name Is: Mohammed Alaa Mohsen
# print(member_three.get_all_info()) # Hello Mr.Karrem, Your Full Name Is: Karrem Abd Fiez
# print(member_four.get_all_info()) # ValueError: Name Not Allowed

print(Member.user_num) # 4 -> من الكلاس اربع مرات اصبح عدد المستخدمين أربعة(Objects) Instance Methods الأن بعد ما اعملت استدعاء لل

print(member_four.delete_user()) # User Hell Is Deleted :(

print(Member.user_num) # 3
