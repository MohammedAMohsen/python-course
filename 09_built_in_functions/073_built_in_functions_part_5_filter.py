# Lesson 073 - Built In Functions Part 5 Filter
# Video: https://www.youtube.com/watch?v=0Zmdu7OgVl0

# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Keeps Only The Elements For Which The Function Returns True
# [5] The Function Need To Return Boolean Value

# Bool Value (True, False) ولكن الفرق فيه انو يستقبل Map()ببساطة يشبه ال
# بعملها فلتر وما برجعها او يطبعها False برجعها او بطبعها لو True لو 

# ---------------------------------------------------------------

# ============ Example 1 ============

def checkNumber(Num):
    if Num > 10:
        return Num
#       return True وليس مع قيم bool value الأصح اني اقلو هيك لانو الفلتر يتعامل مع

MyNamber = [1,19,10,20,100,5]

myResult = filter(checkNumber, MyNamber)

for num in myResult:

    print(num)

# ----------- معلومة ع الماشي ---------------------

# لو كان الشرط يساوي صفر يعني رجع القيم الي تساوي صفر

def checkNumber2(Num2):
    if Num2 == 0:
#       return Num هيك مش يطبع اشي
        return True 

MyNamber2 = [0,0,1,19,10,20,100,5,0]

for num2 in filter(checkNumber2, MyNamber2):
    print(num2)

# ! لاحظ مش هيرجع اشي معنو الشرط الصح
# عشان هيك ما برجعو False والصفر عبارة عن False او True لازم تعرف انو الفلتر برجع 
# bool لانو الفلتر برجع return = True لحل المشكلة بخلي ال
# والأن بعد التعديل برجع الثلاث اصفار الي وجدهم

# -------------------------------------------------

# اختصارا لما سبق لاحظ المثال التالي وطريقة كتابة الشرط بالطريقة التي يعمل بها الفلتر بشكل ابسط واصح

def checkNumber3(Num3):

    return Num3 > 10 # هو يتعامل مع صح او خطأ اذا صح رجع القيمة الي تساوي الشرط واذا خطأ ما ترجع اشي

MyNamber3 = [1,19,10,20,100]

for num3 in filter(checkNumber3, MyNamber3):

    print(num3)

# ============ Example 2 ============

def checkName(name):
    return name.startswith("o")

listName = ["mohammed", "ahmed", "osame", "maha", "ola"]

for name in filter(checkName,listName):
    print(name)

# ===== Example 3: With Lambda ======

for name in filter(lambda name: name.startswith("m"),listName):
    print(name)
