# Lesson 082 - Generators
# Video: https://www.youtube.com/watch?v=QNN3w7Na7HA

# ----------------
# -- Generators -- (المولدات)
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Beginning
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def MyFun():
    return 1

def MyGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

print(type(MyFun())) # <class 'int'>
print(type(MyGenerator())) # <class 'generator'>

# -------------------------------------

myGen = MyGenerator()

print(next(myGen))

print("Hello From Python")

print(next(myGen))

print("Hello From bla bla bla")

print(next(myGen))

print("Goooood")

print(next(myGen))

# 1
# Hello From Python
# 2
# Hello From bla bla bla
# 3
# Goooood
# 4

# هي هي فائدة او طريقة عمل الإنتريتور و الجنريت وهي بدون ما اعمل لووب
# او العناصر الي عندي الي بدي اعمل عليهم لووب Iterableبعطيني تحكم كامل في الوصول لل
# وفي كل استدعاء للجريتور بكمل من آخر نقطة وصللها وما بعيد من الأول
# زي المثال السابق

for number in myGen:
    print(number)

# الحلقة السابقة لن تطبع شيئا
# لأن المولد أعطانا كل قيمه في الأعلى بالأمر next ووصل إلى النهاية
# المولد يستخدم مرة واحدة فقط، ولو أردنا الطباعة من جديد ننشئ مولدا جديدا

# myGen = MyGenerator()
# for number in myGen:
#     print(number)

# 1
# 2
# 3
# 4

# Example على ما سبق

def MyGeneratorTwo():
    yield "One"
    yield "Two"
    yield "Three"
    yield "Four"
    yield "Five"

myGenTwo = MyGeneratorTwo()

print(next(myGenTwo))
print(next(myGenTwo))
print(next(myGenTwo))

print("-"*30)

for txt in myGenTwo:
    print(txt)

# One
# Two
# Three
# ------------------------------
# Four
# Five

# لاحظ طبع اول ثلاث عناصر وبعدها في الفور كمل باقي العناصر الي هم العنصرين الباقين
