# Lesson 070 - Built In Functions Part Two
# Video: https://www.youtube.com/watch?v=2ed3aomFliA

# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable(إجباري), start(إختياري))

a = [1, 10, 19, 40]

print(sum(a)) # 70
print(sum(a, 10)) # 80 / start => القيمة الإفتراضية له 0 وهو عبارة الرقم الذي يبدأ من عنده الجمع مع باقي الأرقام

# --------------------------------------------------------------------------

# round(number, numofdigits(إختياري))

print(round(122.499)) # 122
print(round(122.599)) # 123
print(round(122.6553455, 2)) # 122.66 / numofdigits => عدد المنازل الي هطبعها بعد الرقم العشري

# --------------------------------------------------------------------------

# range(start(إختياري) = 0, end(إجباري), step(اختياري) = 1)

print(list(range(0))) # []
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] Endلانو القيمة اجبارية في طبيعي الرقم يكون هو ال Endاعتبر ال10 هي ال
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
print(list(range(1, 11, 2))) # [1, 3, 5, 7, 9]

# --------------------------------------------------------------------------

# print(sep)

print("Hello Osama") # Hello Osama # هادي عبارة عن رسالة واحدة
print("Hello","Osama") # Hello Osama # هادي عبارة عن رسالتين والقيمة الافتراضية للفصل بين الرسالتين هي المسافة
print("Hello","Osama","How","Are","You") # Hello Osama How Are You
print("Hello","Osama","How","Are","You", sep="|") # Hello|Osama|How|Are|You هان انا غيرت القيمة الفتراضية لجميع بين الرسائل من مسافة الى الرمز السابق

# الفائدة منه انو لو بدي اكتب اكثر من رسالة في جملة الطباعة ,ما أقعد افصل بينهم بشكل يدوي, هذة الطريقة أسهل وأبسط

# --------------------------------------------------------------------------

# print(end)

print("First Line")
print("Second Line")

# First Line
# Second Line

print("First Line", end="\n") # end = "\n" هذة القيمة الإفتراضية لما بعد أمر الطباعة
print("Second Line", end="\n")
# First Line
# Second Line

print("First Line", end=" * ") # هان أنا غيرت القيمة الافتراضية من انو يبدأ سطر جديد الى علامة النجمة
print("Second Line")
# First Line * Second Line

print("First Line", end=" .... ") 
print("Second Line", end=" .... ")
print("Third Line")
print("Four Line")
# First Line .... Second Line .... Third Line
# Four Line
# # آخر جملة طباعة لذلك بدأ الجملة الثالثة بنفس السطر لجمل السابقة End هو بطبع حسب 
