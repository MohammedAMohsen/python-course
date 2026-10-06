# Lesson 086 - Practical Loop On Many Iterators With Zip
# Video: https://www.youtube.com/watch?v=Z1gwFze9e94

# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------

list1 = [2, 6, 1, 0, 10, 3]
list2 = ["A", "B", "C"]
tuple1 = ("Man", "Woman", "Girl", "Boy", "GameOver")
dict1 = {"Name": "Mohammed", "Age": 23, "Country": "Gaza", "Skills" : "Zip"}

ultimateList = zip(list1, list2)

print(ultimateList) # <zip object at 0x78baf5603d80> -> العنوان يختلف في كل تشغيل

for item in ultimateList:
    print(item)

# (2, 'A')
# (6, 'B')
# (1, 'C')

# -----------------------------

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

    print("List 1 Item => ", item1)
    print("List 2 Item => ", item2)
    print("Tuple 1 Item => ", item3)    
    print("Dict 1:",item4, " => ", dict1[item4])    

# List 1 Item =>  2
# List 2 Item =>  A
# Tuple 1 Item =>  Man
# Dict 1: Name  =>  Mohammed
# List 1 Item =>  6
# List 2 Item =>  B
# Tuple 1 Item =>  Woman
# Dict 1: Age  =>  23
# List 1 Item =>  1
# List 2 Item =>  C
# Tuple 1 Item =>  Girl
# Dict 1: Country  =>  Gaza

# لماذا ؟؟ list or Tuple لاحظ في كل مرة بيأخذ 3 عناصر من كل مجموعة او من كل 
# بطبع عناصر المجموعات بناء على عدد او طول أقل مجموعة Zipلانه هذه هي آلية عمل ال
# يعني اقل مجموعة فيها 3 عناصر, بطبع 3 عناصر فقط من باقي المجموعات
# لو اقل مجموعة فيها عنصرين, بطبع عنصرين فقط من باقي المجموعات
