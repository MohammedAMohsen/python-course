# Lesson 009 - Escape Sequences Characters
# Video: https://www.youtube.com/watch?v=cr2Nk2E0f5A

# ----------------------------
# Escape Sequences Characters
# \b => Back Space                  بحذف على مقدار حرف
# \newline => Escape New Line + \   يسمح بالنزول سطر الى الأسفل أثناء الكتابة وليس في الناتج
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed                    يسمح بالنزول سطر للأسفل أثناء الطباعة
# \r => Carriage Return              تقوم بنقل الأحرف الي بعدها إلى الخلف وإستبدالهم حسب عددهم
# \t => Horizontal Tab               بعمل مسافة كبيرة 
# \xhh => Character Hex Value        Hexيسمح بكتابة بستخدام رموز ال
# ----------------------------


# Back Space
print("Hello\bWorld") # Will Remove o -> HellWorld


# Escape New Line +\
print("Hello \
I Love \
Python")

# Escape Back Slash (\)
print("I Love Back Slash \\")

# Escape Single Quote (')
print('I Love Single Quote \'Test\' ')

# Escape Double Quote (")
print("I Love Double Quote \"Test\" ")

# Escape Line Feed
print("Hello World\nSecond Line") 

# Carriage Return
print("12345678\rabcd") # Output => abcd5678
# ملاحظة: تأثير الرمزين \b و \r يظهر فقط عند التشغيل في الطرفية

# Horizontal Tab
print("Hello\tPython") 

# Character Hex Value
print("\x4D\x4F\x48\x41\x4D\x4D\x45\x44") # MOHAMMED
