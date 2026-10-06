# Lesson 032 - Dictionary Methods Part Two
# Video: https://www.youtube.com/watch?v=rgOdxQa830Q

# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
    "name" : "Mohammed"
}

print(user) # {'name': 'Mohammed'}
print(user.setdefault("name", "Ahmed")) # Mohammed -> هل الإسم موجود , نعم خلص بطبع الإسم الي موجود في الأصل
print(user) # {'name': 'Mohammed'}

print(user) # {'name': 'Mohammed'}
print(user.setdefault("age", 21)) # 21 -> هل العمر موجود , لا بضيفو وبطبع قيمتو
print(user) # {'name': 'Mohammed', 'age': 21}

# popitem() -> Dictionaryبرجع آخر عنصر أو قيمة ضفتها بال

member = {
    "name" : "Mohammed",
    "age" : 21,
    "country" : "Gaza",
}

print(member.popitem()) # ('country', 'Gaza')
member.update({"skill" : "PS4"})
print(member.popitem()) # ('skill', 'PS4')

# items()

view = {
    "name" : "Osama",
    "skill" : "XBox"
}

allItems = view.items()
print(view) # {'name': 'Osama', 'skill': 'XBox'}
view["age"] = 36

print(allItems) # dict_items([('name', 'Osama'), ('skill', 'XBox'), ('age', 36)])
# allItems <- Dictionaryلاحظ أنو حتى بعد عملية التحديث والإضافة تمت إضافة هذة التحديثات في ال
# Tuple والقيم عبارة عن List أيضا لاحظ الناتح من العملية السابقة عبارة عن 

# fromkeys() -> قمت بإنشائه vareble بعين مفاتيح وقيمة لها من 

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = ("X")

print(dict.fromkeys(a, b)) # {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'} 
