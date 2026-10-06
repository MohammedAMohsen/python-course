# Lesson 104 - OOP Part 2 - Class Syntax And Info
# Video: https://www.youtube.com/watch?v=Sphiyp42cp0

# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Constructor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function

class Member:

    def __init__(self):

        print("A New Member Has Been Added")


Member() # A New Member Has Been Added

print(dir(Member)) # اعرض محتويات الكلاس

member_one = Member()   # A New Member Has Been Added
member_two = Member()   # A New Member Has Been Added
member_three = Member() # A New Member Has Been Added

# عشان اعرف البيانات لاي كلاس عندي
print(member_one.__class__) # <class '__main__.Member'>  # Memberبقلي انو هاد تابع لكلاس ال
