# Lesson 013 - Strings Methods Part One
# Video: https://www.youtube.com/watch?v=HmDLsnLgt0M

# --------------------------------------------------------
# -- String Methods --------------------------------------
# -- len, strip, title, capitalize, zfill, upper, lower --
# --------------------------------------------------------

# len() بترجع عدد العناصر في جملة معينة

a = "I Love Python"
b = "     I Love Python     "

print(len(a)) # 13
print(len(b)) # 23 => المسافات الي قبل النص وبعده بتنحسب (5 + 13 + 5)

# strip () بتحذف المسافات من ع اليمين والشمال
# rstrip () بتحذف المسافات من ع اليمين
# lstrip () بتحذف المسافات من ع الشمال

b = "     I Love Python     "
c = "######I Love Python#####"
d = "#@#@#@#@I Love Python#@#@#@#@#"

print(b.strip())  # => |I Love Python|
print(b.rstrip()) # => |     I Love Python|
print(b.lstrip()) # => |I Love Python     |
print(len(b.strip())) # => 13
print(len(b.rstrip())) # => 18

# strip() القيمة الإفتارضية داخل الأقواس فارغة , بحذف المسافات , ممكن نضيف قيمة بالرمز أو الشغلة الي هيحذفها فيها

print(c.strip('#'))  # => I Love Python
print(c.rstrip('#')) # => ######I Love Python
print(c.lstrip('#')) # => I Love Python#####

print(d.strip('#@')) # => I Love Python


# title() بحول أول حرف من كل كلمة الى حرف كبير حتى بعد الأرقام

e = "mohammed mohsen 22th basha"
print(e.title()) # => Mohammed Mohsen 22Th Basha

# capitalize() => بحول فقط أول حرف من الجملة الى حرف كبير

f = "mohammed mohsen 22th basha"
print(f.capitalize()) # => Mohammed mohsen 22th basha

# zfill() => برتب نسق الأرقام سواء كانت الأحادية والعشرية والمئوية

g, h, i, j = "1", "11", "111", "1111"
print(g)
print(h)
print(i)
# 1
# 11
# 111
print(g.zfill(4))
print(h.zfill(4))
print(i.zfill(4))
print(j.zfill(4))
# 0001
# 0011
# 0111
# 1111

# upper() بحول الأحرف لكل الكلمات والجمل الى حروف كبيرة
# lower() بحول الأحرف لكل الكلمات والجمل الى حروف صغيرة

k = "mohammed mohsen"
l = "MOHAMMED MOHSEN"

print(k.upper()) # => MOHAMMED MOHSEN
print(l.lower()) # => mohammed mohsen
