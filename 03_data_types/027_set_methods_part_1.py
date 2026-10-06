# Lesson 027 - Set Methods Part One
# Video: https://www.youtube.com/watch?v=N06_D5wWobg

# -----------------
# -- Set Methods --
# -----------------

# ---- clear() ----

a = {1, 2, 3, 4}
a.clear()

print(a) # set()

# ---- union() ----

b = {"One", "Two", "Three"}
c = {1, 2, 3}
d = {"AlBasha", "Elzero"}

print(b.union(c))     # {1, 'One', 'Two', 2, 3, 'Three'} -> Concatenationزي ال
print(b.union(c,d))   # {1, 'One', 'Two', 2, 3, 'AlBasha', 'Three', 'Elzero'}
print(b | c)          # {'One', 1, 2, 3, 'Two', 'Three'} -> (|)طريقة ثانية بستخدام ال

# ---- add() ----

e = {1, 2, 3, 4}

e.add(5) # -> بضيف عنصر, يمكن إضافة عنصر عنصر , يعني ما بنفع أدخل قيمتين في نفس الوقت داخل الميثود 
print(e) # {1, 2, 3, 4, 5}

# ---- copy() ----

f = {1, 2, 3, 4}

g = f.copy() # -> بعمل نسخة, والنسخة الجديدة ما إلها علاقة بالنسخة الأصلية
print(g) # {1, 2, 3, 4}

# ---- remove() ----

h = {1, 2, 3, 4}

h.remove(1)
print(h)  # {2, 3, 4}
# h.remove(7) Error -> لانو العنصر الي بدو يحذفو مش موجود

# ---- discard() ----

i = {1, 2, 3, 4}

i.discard(1)
print(i) # {2, 3, 4}
i.discard(7) # -> remove و discard لاحظ العنصر مش موجود ومع ذلك ما طلعلي رسالة خطأ , لانو هاد الفرق بين ال

# ---- pop() ----


j = {"A", True, 1, 2, 3, 4, 5}

print(j.pop()) # -> بيخرج عنصر بشكل عشوائي لأنو ما بنفع أعطيلو عنصر معين

# ---- update() ----

k = {1, 2, 3}
l = {1, "A", "B", 2}

k.update(l) # -> مع بعض وطبعا بحذف المكرر Setsبجمع ال unionزي ال
k.update(["One","Two"]) # -> Setعشان يضيفهم داخل ال Updateبزبط أضيف قائمة داخل ال 

print(k) # {'B', 1, 2, 3, 'One', 'Two', 'A'}

