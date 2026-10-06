# Lesson 034 - Boolean Operators
# Video: https://www.youtube.com/watch?v=zN6ZYGSBKbM

# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 21
country = "Gaza"
rank = 10

print(age > 16) # True
print(country == "Gaza") # True

# and -> لازم جميع الشروط تتحقق

print(age > 16 and country == "Gaza" and rank > 0) # True
print(age > 16 and country == "USA" and rank > 0) # False

# or -> لا يشترط على جميع الشروط أن تتحقق, (على الأقل واحد)

print(age > 16 or country == "Gaza" or rank > 0) # True
print(age > 16 or country == "USA" or rank > 0) # True
print(age > 16 or country == "USA" or rank > 20) # True
print(age > 40 and country == "USA" or rank > 20) # False

# not -> 🔁 بتعكس الجواب

print(age > 16) # True
print(not(age > 16)) # False -> Not True = False
print(not(rank > 30)) # True
