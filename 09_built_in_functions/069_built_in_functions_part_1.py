# Lesson 069 - Built In Functions Part One
# Video: https://www.youtube.com/watch?v=-PfCcZ2Q_MI

# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------
x = [1, 2, 3, 4, []]

if all(x): # يعني كل العناصر صحيحة
    print("All Elements Is True")

else: # elseفي حال كان أحد العناصر خطاء يطبع ال
    print("Theres At Least One Element Is False")

#-----------------------------

if any(x): # اي عنصر صحيح يعني (على الأقل عنصر واحد)
    print("There's At Least One Element Is True")

else: # elseفي حال كان كل العناصر خطاء يطبع ال
    print("Theres No Any True Elements")

#-----------------------------

# bin(): بحول اي رقم الى صفر وواحد (لغة الحاسوب)

print(bin(230)) # 0b11100110

#-----------------------------

# id() لكل عنصر عندي Memoryالعنوان الي بنحجز في ال
# ملاحظة: الأرقام التالية تختلف من جهاز لآخر ومن تشغيل لآخر

a = 1
b = 2

print(id(a)) # 140718766773160
print(id(b)) # 140718766773192
print(id(b) + id(a)) # 281437533546352
