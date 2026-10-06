# Lesson 045 - Membership Operators
# Video: https://www.youtube.com/watch?v=FGnMK1y9TkE

# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Mohammed"
print("s" in name) # False => موجود sهل حرف ال
print("m" in name) # True
print("D" in name) # False => حساس لحالة الأحرف

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends) # False
print("Ahmed" in friends) # True
print("Mahmoud" not in friends) # False

# Using In And Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "USA"

# if myCountry == "Egypt" or myCountry == "KSA" or myCountry == "Kuwait" : 
#     print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
# else :
#     print("You Have No Discount")

if myCountry in countriesOne: # -> إذا كانت هذة المدينة موجودة في قائمة المدن إعمل كذا \ أفضل ما أقعد أعدد بالدول زي فوق
    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
elif myCountry in countriesTwo:
    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")
else:
    print("You Have No Discount")
