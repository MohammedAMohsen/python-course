# Lesson 047 - Loop - While and Else
# Video: https://www.youtube.com/watch?v=A0oBGPSUbeI

# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0
while a < 10:
    print(a) # 0 1 2 ... 9
    a += 1
else:
    print("Loop Is Done") # True Become False

# ------------------------------------------------------

b = 0
while b < 10:
    print(b) # 0 1 2 ... 9
    b += 1
print("Loop Is Done") #  elseممكن بدون إستخدام ال

# ------------------------------------------------------

while False:
    print("Will Not Print")
