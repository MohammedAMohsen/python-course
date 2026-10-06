# Lesson 090 - Errors And Exceptions Raising
# Video: https://www.youtube.com/watch?v=5umR9zAidoc

# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------
# ملاحظة: هذا الملف يتوقف عند أول خطأ بشكل مقصود
# لتجربة المثال الذي بعده، ضع علامة # أمام سطر raise الذي توقف عنده
# -----------------------------------------------------------------

x = -10

if x < 0:

    print(f"the number {x} is less than zero")

else:

    print(f"{x} is good number and ok")


print("print message after if condition")

# Output

# the number -10 is less than zero
# print message after if condition
# لاحظ بكمل البرنامج طبيعي, لانو ما مسك خطأ عشان يوقف البرنامج
# في المثال التالي انا هعرف انو الإشي الي اقل من 0 هو عبارة عن خطأ ولازم يقف البرنامج

# ----------------------------

x = -10

if x < 0:

    raise Exception(f"the number {x} is less than zero")

else:

    print(f"{x} is good number and ok")


print("print message after if condition")
print('pla pla pla ...')

# Output

# Traceback (most recent call last):
#   File "/home/user/python-course/14_errors_and_debugging/090_errors_and_exceptions_raising.py", line 44, in <module>
#     raise Exception(f"the number {x} is less than zero")
# Exception: the number -10 is less than zero
# لاحظ ان باقي الكود في البرنامج لن يظهر لان البرنامج توقف ولن يكمل بعد ان عمل اكسبشن

# ----------------------------

# Example 2:

y = "Mohammed"

if type(y) != int:

    raise ValueError("Only Numbers Allowed")

print('print message after if condition')
print('pla pla pla ...')


# Output

# Traceback (most recent call last):
#   File "/home/user/python-course/14_errors_and_debugging/090_errors_and_exceptions_raising.py", line 70, in <module>
#     raise ValueError("Only Numbers Allowed")
# ValueError: Only Numbers Allowed

# Error Value اعمل Exception ممكن بدل ما اعمل 

# ----------------------------

f = 4

if type(f) != int:

    raise ValueError("Only Numbers Allowed")

print('print message after if condition')
print('pla pla pla ...')

# في حال ما كان خطأ بكمل البرنامج طبيعي

# Output

# print message after if condition
# pla pla pla ...
