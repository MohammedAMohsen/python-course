# Lesson 106 - OOP Part 4 - Instance Attributes And Methods Part 2
# Video: https://www.youtube.com/watch?v=ImXpb95dXGc

# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Member:

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender 


    def full_name(self):
        
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

        # Attributesوال Methodsالي داخل الكلاس عندي بتقدر تعمل وصول لكل من ال Instance Methods



member_one = Member("Mohammed", "Alaa", "Mohsen", "Male")
member_two = Member("Mona", "Vozi", "Hassona", "Female")
member_Three = Member("Ali", "Osama", "Alshame", "g")

# print(member_one.fname, member_one.mname, member_one.lname) # Mohammed Alaa Mohsen
# print(member_two.fname) # Mona

print(member_one.full_name()) # Mohammed Alaa Mohsen

print(member_one.name_with_title()) # Hello Mr.Mohammed
print(member_two.name_with_title()) # Hello Miss.Mona
print(member_Three.name_with_title()) # Ali

print(member_one.get_all_info()) # Hello Mr.Mohammed, Your Full Name Is: Mohammed Alaa Mohsen
print(member_two.get_all_info()) # Hello Miss.Mona, Your Full Name Is: Mona Vozi Hassona

