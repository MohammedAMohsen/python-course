# Lesson 089 - Installing And Use Pylint For Better Code
# Video: https://www.youtube.com/watch?v=YvqKqam_3zY

# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------

# pip install pylint

# عن طريقة بعلمنا او بوجهنا كيف نكتوب كود نظيف ومتوافق مع المعايير
# وبصلح الأخطاء الي بتكون عندي في المشروع
# هو ما بظهر الأخطاء في الكود ولكن بوجهك لتكتب كود سليم بستايل نظيف
# على سبيل المثال بطريقة احترافية varibel or func يعني بالمختصر بعلمني كيف اكتب اسم ال

def sayHello(name):

    msg = "hello"
 
    return f"{msg} {name}"

print(sayHello("Ahmed"))

# احفظ الكود السابق وحده في ملف باسم hello_bad.py ثم شغل الأمر التالي في الطرفية
# pylint hello_bad.py

# ************* Module hello_bad
# hello_bad.py:4:0: C0303: Trailing whitespace (trailing-whitespace)
# hello_bad.py:8:0: C0305: Trailing newlines (trailing-newlines)
# hello_bad.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# hello_bad.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
# hello_bad.py:1:0: C0103: Function name "sayHello" doesn't conform to snake_case naming style (invalid-name)

# -----------------------------------
# Your code has been rated at 0.00/10


# == =============================== ==
# == --------- albasha.py ---------- == ملف جديد بتسمية مناسبة وطريقة كتابة كود منسق حسب المعيار المتفق عليه
# == =============================== ==

"""
This Is My Module
To Create Function
To Say Hello
"""

def say_hello(name):

    """This function returns a greeting message."""

    msg = "hello"

    return f"{msg} {name}"

say_hello("Ahmed")

# pylint albasha.py

# ------------------------------------
# Your code has been rated at 10.00/10
