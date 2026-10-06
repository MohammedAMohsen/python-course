# Lesson 151 - Virtual Environment Part 2
# Video: https://www.youtube.com/watch?v=holkKfN7qhY

# ----------------------------------------
# -- Virtual Environment => Part 2 --------
# ----------------------------------------
# بعد تفعيل البيئة، أي مكتبة نثبتها تذهب إلى البيئة فقط
# والملف requirements.txt يحفظ أسماء المكتبات وإصداراتها حتى يعيد أي شخص بناء نفس البيئة
# ----------------------------------------
# الأوامر التالية تكتب في الطرفية والبيئة مفعلة
# ----------------------------------------

# pip install ascii-train                # تثبيت مكتبة داخل البيئة
# pip freeze                             # عرض المكتبات المثبتة مع أرقام إصداراتها
# pip freeze > requirements.txt          # حفظ القائمة السابقة في ملف
# pip install -r requirements.txt        # تثبيت كل المكتبات الموجودة في الملف دفعة واحدة

# مثال: هذا الملف يعمل فقط إذا كانت المكتبة مثبتة في البيئة المفعلة
# بدونها يظهر الخطأ: ModuleNotFoundError: No module named 'ascii_train'

import ascii_train

ascii_train.train("AlBasha") # يعرض قطارا متحركا في الطرفية يحمل الكلمة
