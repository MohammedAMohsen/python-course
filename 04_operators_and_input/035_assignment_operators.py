# Lesson 035 - Assignment Operators
# Video: https://www.youtube.com/watch?v=mvyEHxIX_lE

# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------

x = 20
y = 10
x += y
print(x) # 30

x = 20
y  = 10
x -= y
print(x) # 10

x = 20
y  = 10
x *= y
print(x) # 200

x = 20
y = 10
x /= y
print(x) # 2.0 -> القسمة تعطي دائما عددا عشريا

x = 2
x **= 3
print(x) # 8 -> 2 * 2 * 2

x = 22
x %= 5
print(x) # 2 -> باقي القسمة

x = 22
x //= 5
print(x) # 4 -> القسمة بدون الكسور
