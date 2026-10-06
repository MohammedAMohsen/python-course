# Lesson 030 - Dictionary
# Video: https://www.youtube.com/watch?v=BQ7jFrysbQU

# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] You Access Dict Element With Key Not Index
# ملاحظة: منذ الإصدار 3.7 القاموس يحافظ على ترتيب الإضافة
# لكن الوصول للعناصر يكون بالمفتاح فقط وليس برقم الموقع
# ----------------------------

# Dictionary

user = {
    "Name" : "Mohammed",
    "Age" : 21,
    "Country" : "Gaza",
    # [1, 2, 3] : "Test" -> بنسبه للمفتاح (List) ما بتقبل قوائم 
    (1, 2, 3) : "Test", # -> (Tuple)بتقبل ال 
    "Skills" : ["Html", "Css", "Js"], # -> (List) بنفع يكون القيمة عبارة عن 
    "Rating" : 30.4,
    "Name" : "Ahmed" # -> ما بنفع أكرر المفتاح , في الحالة هادي هيحدث قيمة الإسم من محمد ل أحمد
}

print(user)
# {'Name': 'Ahmed', 'Age': 21, 'Country': 'Gaza', (1, 2, 3): 'Test', 'Skills': ['Html', 'Css', 'Js'], 'Rating': 30.4}

# عشان أوصل لعنصر معين ببحث عنو بمفتاحو فقط

print(user['Age']) # 21
print(user['Skills']) # ['Html', 'Css', 'Js']
# OR
print(user.get("Skills")) # ['Html', 'Css', 'Js']
print(user.get("Progress","None")) # None -> مفيدة إني بعطيلو قيمة إفتراضية لو ما وجد المفتاح في القاموس get

# ممكن أطبع جميع المفاتيح أو جميع القيم

print(user.keys()) # dict_keys(['Name', 'Age', 'Country', (1, 2, 3), 'Skills', 'Rating'])
print(user.values()) # dict_values(['Ahmed', 21, 'Gaza', 'Test', ['Html', 'Css', 'Js'], 30.4])

print(len(user)) # 6

# Two Dimensional Dictionary

languages = {
    "One" : {
        "Name" : "Html",
        "Progress" : "80%"
    },
    "Two" : {
        "Name" : "Css",
        "Progress" : "90%"
    },
    "Three" : {
        "Name" : "Js",
        "Progress" : "90%"
    }
    }

print(languages)
# {'One': {'Name': 'Html', 'Progress': '80%'}, 'Two': {'Name': 'Css', 'Progress': '90%'}, 'Three': {'Name': 'Js', 'Progress': '90%'}}

print(languages['One']) # {'Name': 'Html', 'Progress': '80%'}
print(languages['Two']) # {'Name': 'Css', 'Progress': '90%'} 

print(languages['Three']['Name']) # Js 

# Dictionary Length

print(len(languages)) # 3
print(len(languages["One"])) # 2

# Create Dictionary From Variables

frameworkOne = {
    "Name" : "Vuejs",
    "Progress" : "80%"
}

frameworkTwo = {
    "Name" : "ReactJs",
    "Progress" : "90%"
}

frameworkThree = {
    "Name" : "Angular",
    "Progress" : "50%"
}

allFramework = {
    "One" : frameworkOne,
    "Two" : frameworkTwo,
    "Three" : frameworkThree
}

print(allFramework)
print(allFramework["One"]) # {'Name': 'Vuejs', 'Progress': '80%'}
print(allFramework["Two"]["Progress"]) # 90%
