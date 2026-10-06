# Lesson 011 - Strings
# Video: https://www.youtube.com/watch?v=j0Wktr70Cgw

# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

myStringThree = 'This is Single Quote "Test" '
myStringFour = "This is Double Quotes 'Test' "
myStringFive = "This is Double Quotes \"Test\" "

# \nنفس فكرة ال --> myStringSix = 'First\nSecond\nThird'
myStringSix = '''First
Second
Third'''
myStringSeven = """First
Second
Third"""
myStringEight = """First
Second "Test" 'Test'
Third"""
# بتعمل سكيب لأي أشي داخلها سواء حروف خاصة أو أسطر أو علامات تنصيص """ or ''' علامة التنصيص هادي
# تصحيح: علامات التنصيص الثلاثية تسمح بكتابة علامات التنصيص والأسطر الجديدة بحرية
# لكن الشرطة المائلة تبقى رمز هروب داخلها، ولكتابتها كما هي نكتبها مرتين

print(myStringOne)
print(myStringTwo)
print(myStringThree)
print(myStringFour)
print(myStringFive)
print(myStringSix)
print(myStringSeven)
print(myStringEight)
