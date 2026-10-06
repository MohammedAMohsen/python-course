# Lesson 028 - Set Methods Part Two
# Video: https://www.youtube.com/watch?v=o8pr--y5vuU

# -----------------
# -- Set Methods --
# -----------------

# difference() -> بجيب الفرق بين المجموعتين , يعني إيش الموجود في المجموعة الأولى ومش موجود في المجموعة الثانية

a = {1, 2, 3, 4}
b = {1, 2, "Mohammed", "Ahmed"}

print(a) # {1, 2, 3, 4}
print(a.difference(b)) # {3, 4} => or a - b
print(a) # {1, 2, 3, 4}

# difference_update() -> بحدث المجموعة بالقيم الي مش موجودة بالمجموعة الثانية

c = {1, 2, 3, 4}
d = {1, 2, "Mohammed", "Ahmed"}

print(c) # {1, 2, 3, 4}
c.difference_update(d) # -> a - b
print(c) # {3, 4} 

# intersection() -> بجيب العناصر المشتركة بين المجموعتين

e = {1, 2, 3, 4, "X"}
f = {"Mohammed", "X", 2}

print(e) # {1, 2, 3, 4, 'X'}
print(e.intersection(f)) # {2, 'X'} => e & f
print(e) # {1, 2, 3, 4, 'X'}

# intersection_update() -> بحدث المجموعة الأولى بالقيم المشتركة في المجموعة الثانية فقط

g = {1, 2, 3, 4, "X"}
h = {"Mohammed", "X", 2}

print(g) # {1, 2, 3, 4, 'X'}
g.intersection_update(h) # -> e & f
print(g) # {2, 'X'}

# symmetric_difference() ->أيش في عناصر مش موجودة في المجموعة الأولى بالنسبة للمجموعة الثانية 
# وإيش في عناصر مش موجودة في المجموعة الثانية بالنسبة للمجموعة الأولى

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4}

print(i) # {1, 2, 3, 4, 5, 'X'}
print(i.symmetric_difference(j)) # {3, 5, 'Zero', 'X', 'Osama'} => or i ^ j
print(i) # {1, 2, 3, 4, 5, 'X'}

# symmetric_difference_update() -> بحدث المجموعة بالقيم الي مش موجودة في المجموعة الثانية بالنسبة للمجموعة الأولى 
# والقيم الي مش موجودة في المجموعة الأولى بنسبة للمجموعة الثانية

k = {1, 2, 3, 4, 5, "X"}
m = {"Osama", "Zero", 1, 2, 4}

print(k) # {1, 2, 3, 4, 5, 'X'}
k.symmetric_difference_update(m) # -> or i ^ j
print(k) # {3, 5, 'X', 'Osama', 'Zero'}
