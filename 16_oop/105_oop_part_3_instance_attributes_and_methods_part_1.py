# Lesson 105 - OOP Part 3 - Instance Attributes And Methods Part 1
# Video: https://www.youtube.com/watch?v=YNm5Go1NM9M

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

    def __init__(self, name, age, country):

        self.hello = "Hello"
        self.name = name
        self.age = age
        self.country = country


member_one = Member("Mohammed",23, "Gaza")

# print(dir(member_one))# => الي ضفناها ... , age , nameال Methodالخاصة الي عملناها وهتلاحظ وجود  Instanceالخاصة بال Attributesهيعرض جميع ال

print(member_one.hello) # Hello
print(member_one.name) # Mohammed
print(member_one.age) # 23
print(member_one.country) # Gaza

member_two = Member("Ahmed", 50, "Qatar")

print(member_two.hello) # Hello
print(member_two.name) # Ahmed
print(member_two.age) # 50
print(member_two.country) # Qatar
