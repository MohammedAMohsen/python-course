# Lesson 031 - Dictionary Methods Part One
# Video: https://www.youtube.com/watch?v=oNLaNJrU8r8

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
    "name" : "Mohammed"
}

print(user)
user.clear()
print(user) # {}

# update()

member = {
    "name" : "Mohammed"
}

print(member) # {'name': 'Mohammed'}
member["age"] = 36                           # -> ممكن أضيف أو أحدث البيانات بهادي الطريقة
member.update({"name" : "Basha"})            # -> أو بستخدام هادي الطريقة بستخدام الميثود
print(member) # {'name': 'Basha', 'age': 36}

# copy -> عمل نسخة

main = {
    "Name" : "Mohsen"
}
b = main.copy()
print(b) # {'Name': 'Mohsen'}

# keys() + values()

print(main.keys()) # dict_keys(['Name'])
print(main.values()) # dict_values(['Mohsen'])
