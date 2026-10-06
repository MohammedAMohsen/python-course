# Lesson 014 - Strings Methods Part Two
# Video: https://www.youtube.com/watch?v=doDJDkUOEJQ

# ------------------------------------------------------------------
# -- Strings Methods -----------------------------------------------
# -- split, rsplit, center, count, swapcase, startswith, endswith --
# ------------------------------------------------------------------

# split() rsplit() => Listبتاخد الجملة وبتقطعها لعناصر وبتحولها ل
# القيمة الإفتارضية داخل القوسين فاضية معناتو بقطع حسب المسافة
a = "I Love Python and PHP and MySQL"
print(a.split()) # => ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-")) # => ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3)) # => ['I', 'Love', 'Python', 'and-PHP-and-MySQL'] بقطع بمقدار 3 مرات ; أي 4 عناصر

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3)) # => ['I-Love-Python-and', 'PHP', 'and', 'MySQL'] بقطع بمقدار 3 مرات من اليمين ; أي 4 عناصر

# center() => لتزيين, ضوري نضيف القيمة الإفتراضية

e = "AlBasha"
print(e.center(9))  # Spaces      =>  AlBasha 
print(e.center(9, "#"))  # Hashes => #AlBasha#
print(e.center(15, "@"))  # @     => @@@@AlBasha@@@@

# count() => بحسب كم عدد ظهور الحرف أو الكلمة , حساس لحالة الأحرف

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("P"))  # 5 P Later
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

# swapcase() => بحول حالة كل حرف من كبير الى صغير ومن صغير الى كبير

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase()) # => i lOVE pYTHON
print(h.swapcase()) # => I Love Python

# startswith() => يفحص هل تبدأ الجملة بحرف ال.. نعم او لا أيضا حساس لحالة الأحرف

i = "I Love Python"
print(i.startswith("I")) # => True
print(i.startswith("S")) # => False
print(i.startswith("P", 7, 12)) # => True --- من على بعد 7 , نعم Pهل الجملة تبدأ بالحرف 

# endswith() => يفحص هل تنتهي الجملة بحرف ال.. نعم او لا , حساس لحالة الأحرف

j = "I Love Python"
print(j.endswith("n")) # => True
print(j.endswith("S")) # => False
print(j.endswith("e", 2, 6)) # => True --- (Love)من على بعد2 الى 6, نعم eهل الجملة تنتهي بالحرف 
