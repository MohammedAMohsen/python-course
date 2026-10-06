# Lesson 075 - Built In Functions Part 7
# Video: https://www.youtube.com/watch?v=nS-uled9biI

# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "JS", "PHP", "DB"]

mySkillsWitheCounter = enumerate(mySkills, 10) # ببدأ يعد من 10 القيمة الإفتراضية 0

for skill in mySkillsWitheCounter:

    print(skill)

# (10, 'Html')
# (11, 'Css')
# (12, 'JS')
# (13, 'PHP')
# (14, 'DB')

print(type(mySkillsWitheCounter)) # <class 'enumerate'>

# طريقة تغيير التنسيق الخاصة بالعداد

for counter, skill in enumerate(mySkills, 1):

    print(f"{counter} - {skill}")

# 1 - Html
# 2 - Css
# 3 - JS
# 4 - PHP
# 5 - DB

# -----------------------------------------------------

# help() اذا انا ناسي طريقة عملها او مش عارفها function بتساعدني في معرفة ال

help(print) # بتطبع الشرح مباشرة، ولو كتبنا print(help(print)) هيطبع كلمة None في الآخر

# -----------------------------------------------------

# reversed(iterable)

myString = "Albasha"

for l in reversed(myString):
    print(l)

# a
# h
# s
# a
# b
# l
# A

for l in reversed(mySkills):
    print(l)

# DB
# PHP
# JS
# Css
# Html
