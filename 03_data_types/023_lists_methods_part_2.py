# Lesson 023 - Lists Methods Part Two
# Video: https://www.youtube.com/watch?v=pP0QJbJalik

# -------------------
# -- Lists Methods --
# -------------------

# clear() -> بمسح جميع العناصر في القائمة

a = [1, 2, 3, 4]

a.clear()

print(a) # []

# copy -> بتعمل نسخة للقائمة

b = ["One", "Two", "Three", "Four"]

c = b.copy()

print(b) # Main List -> ['One', 'Two', 'Three', 'Four']
print(c) # Copied    -> ['One', 'Two', 'Three', 'Four']

b.append("Five")

print(b) # Main List -> ['One', 'Two', 'Three', 'Four', 'Five']
print(c) # Copied    -> ['One', 'Two', 'Three', 'Four'] -> هذي عبارة عن نسخة ما إلها علاقة بالأصل بإشي سواء زادت أو نقصت 

# count() -> برجع عدد ظهور العنصر في القائمة

d = [1, 2, 4, 1, 20, 5, 32, 1]

print(d.count(1)) # 3

# index() -> برجع مكان العنصر في القائمة

e = ["Mohammed", "Alaa", "Maha", "Ali", "Osama"]

print(e.index("Maha")) # 2

# insert() -> أنو بضيف في المكان الي أنا بحددو مش في الآخر appendبيختلف عن ال

f = [1, 2, 3, 4, 5, "A", "B"]

f.insert(1, "N") # -> في الموقع الثاني في القائمة N ضيف الحرف 
f.insert(-1, "Z") # -> في الموقع الى قبل الآخير Z ضيف الحرف 
f.insert(len(f), "F") # -> آخر إشي F ضيف الحرف

print(f) # [1, 'N', 2, 3, 4, 5, 'A', 'Z', 'B', 'F']

# pop() -> بحذف وبرجع القيمة المحذوفة

g = [1, 2, 3, 4, 5, "A", "B"]

print(g.pop(4)) # 5 --> ازال العنصر الي بالموقع رقم 4 وهو العنصر الخامس لأن العد يبدأ من صفر
print(g.pop()) # B  --> في حال ما أعطيته رقم الموقع للعنصر بزيل آخر عنصر في القائمة بشكل افتراضي
print(g)  # [1, 2, 3, 4, 'A']
