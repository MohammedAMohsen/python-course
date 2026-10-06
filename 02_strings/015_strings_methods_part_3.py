# Lesson 015 - Strings Methods Part Three
# Video: https://www.youtube.com/watch?v=kgb96E9ogUw

# ---------------------------------------------------------------
# -- Strings Methods --------------------------------------------
# -- index, find, rjust, ljust, splitlines, expandtabs ----------
# -- istitle, isspace, islower, isidentifier, isalpha, isalnum --
# ---------------------------------------------------------------

# index(SubString(إجباري), Start, End) ببحث عن الحرف وبرجع مكانو في الجملة

a = "I Love Python"
print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End) Errorبس في حال ما وجد القيمة برجع -1 بدل index نفس

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Mohammed"
print(c.rjust(13))      # '     Mohammed' --> بطبع بعرض 13 وبكمل باقي العرض بالمسافة
print(c.rjust(13, "-")) # '-----Mohammed' --> هان بكمل بالشحطات

d = "Mohammed"
print(d.ljust(13))      # 'Mohammed     '
print(d.ljust(13, "-")) # 'Mohammed-----'

# splitlines() بقطع حسب الأسطر , كل سطر عنصر 

e = """First Line
Second Line
Third Line"""

print(e.splitlines()) # => ['First Line', 'Second Line', 'Third Line']

f = "First Line\nSecond Line\nThird Line" # -> """ او بال \n نفس الفكرة السابقة سواء بستخدام

print(f.splitlines()) # => ['First Line', 'Second Line', 'Third Line'] 

# expandtabs() => بوسع المسافات حسب الطلب

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(15)) # => Hello          World          I              Love           Python

# istitle() -> هل كل حرف بالجملة ببدأ بحرف كبير 

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # => True
print(two.istitle()) # => False, Because 3g not 3G

# isspace() -> بفحص هل هذة مسافة

three = " "
four = ""
print(three.isspace()) # => True
print(four.isspace())  # => False

# islower() -> هل الأحرف صغيرة

five = 'i love python'
six = 'I Love Python'
print(five.islower()) # => True
print(six.islower())  # => False

# isidentifier() -> هل بنفع يكون معرّف

seven = "Mohammed-mohsen"
eight = "Mohammedmohsen100"
nine = "mohammed--mohsen"
ten = "44mohammedmohsen"

print(seven.isidentifier()) # => False, Because (-) Not Allowed In Names
print(eight.isidentifier()) # => True
print(nine.isidentifier())  # => False, Because (-) Not Allowed In Names
print(ten.isidentifier())   # => False, Because It Starts With Number

# isalpha() -> فقط (A-z) هل هي أحرف من 

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha()) # => True
print(y.isalpha()) # => False

# isalnum() -> أو أرقام (A-z) هل هي أحرف من 

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum()) # => True
print(z.isalnum()) # => True
