# Lesson 058 - Function Packing, Unpacking Arguments
# Video: https://www.youtube.com/watch?v=61i7VvPLVns

# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

# myList = [1, 2, 3, 4]

# print(myList) # [1, 2, 3, 4]
# print(*myList) # 1 2 3 4

# =======================================================

def say_hello(n1, n2, n3, n4):

    peoples = [n1, n2, n3, n4]

    for name in peoples:
        print(f"Hello {name}")

say_hello("Mohammed", "Ahmed", "Osama", "Sayed")

# Hello Mohammed
# Hello Ahmed
# Hello Osama
# Hello Sayed

# say_hello("Mo", "Ah", "Os", "Sa", "Al") # Error -> لأن الدالة معرفة بأربع قيم فقط، فلا تقبل الشخص الخامس
# لحل هذه المشكلة نضع النجمة قبل اسم المعامل، وهكذا تقبل الدالة أي عدد من القيم

# =======================================================

def say_hello2(*peoples): # -> ضيف قد ما بدك , هي فائدة إستخدام النجمة في حال ما عرفت كم عدد الأشخاص مثلا

    for name in peoples:
        print(f"Hello {name}")

say_hello2("Mo", "Ah", "Os", "Sa", "Al", "Gh")

# Hello Mo
# Hello Ah
# Hello Os
# Hello Sa
# Hello Al
# Hello Gh

# =======================================================

def show_details(*skills):

    for ski in skills:
        print(ski)


show_details("Html", "Css")
# Html
# Css
show_details("Html", "Css", "Js", "Java", "Python")
# Html
# Css
# Js
# Java
# Python

# =======================================================

def show_details2(name, *skills):

    print(f"Hello {name} Your Skills Is:")

    for ski in skills:

        print(f"- {ski}")

show_details2("Mohammed", "Python", "Sass", "Java")
show_details2("Ahmed", "MySQL", "Html", "Css", "Js")

# Hello Mohammed Your Skills Is:
# - Python
# - Sass
# - Java
# Hello Ahmed Your Skills Is:
# - MySQL
# - Html
# - Css
# - Js
