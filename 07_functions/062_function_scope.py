# Lesson 062 - Function Scope
# Video: https://www.youtube.com/watch?v=VQHLn1wuDBw

# --------------------
# -- Function Scope --
# --------------------

x = 1 # Global Scope

def one():

    return f"Print Variable From Function Scope {x}"

print(f"Print Variable From Global Scope {x}") # Print Variable From Global Scope 1
print(one()) # Print Variable From Function Scope 1

# # =======================================================================

x = 1 # Global Scope

def two():

    x = 2 # Local Scope -> هذا المتغير موجود داخل الدالة فقط، ولا يغير المتغير الخارجي

    return f"Print Variable From Function Scope {x}"

print(f"Print Variable From Global Scope {x}") # Print Variable From Global Scope 1
print(two())

# # =======================================================================

# x = 1 # Global Scope

def three():

    x = 4

    return f"Print Variable From Function Scope {x}"

print(f"Print Variable From Global Scope {x}") # Print Variable From Global Scope 1
# طبع 1 لأن المتغير الخارجي معرف في الأعلى، أما القيمة 4 فهي خاصة بالدالة فقط
# لو لم يكن هناك متغير خارجي أصلا، لظهر خطأ NameError
print(three()) # Print Variable From Function Scope 4

# =======================================================================

def four():

    global x

    x = 2 # -> عرفت المتغير إكس ع إنو متغير عالمي على مستوى البرنامج

    return f"Print Variable From Function Scope {x}"

def five():

    # x = 10

    return f"Print Variable From Function Scope {x}"


# print(f"Print Variable From Global Scope {x}") # Print Variable From Global Scope 1
# قبل استدعاء الدالة four القيمة ما زالت 1، والتغيير إلى 2 يحدث فقط بعد استدعائها
print(four()) # Print Variable From Function Scope 2
print(f"Print Variable From Global Scope {x}") # Print Variable From Global Scope 2
print(five()) # Print Variable From Function Scope 2
# لو فعلنا السطر x = 10 داخل الدالة five سيطبع 10
# لأن الدالة تبحث عن المتغير داخلها أولا، ثم في الخارج
print(five()) # Print Variable From Function Scope 2 -> Globalبروح وبدور في ال Functionداخل ال xفي حال ما عرفنا ال
