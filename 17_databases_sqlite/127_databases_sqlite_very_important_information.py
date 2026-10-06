# Lesson 127 - Databases - SQLite Very Important Information
# Video: https://www.youtube.com/watch?v=DgaGUpb7ttQ

# --------------------------------------------------------
# -- Databases => SQLite => Very Important Information --
# --------------------------------------------------------

import sqlite3

db = sqlite3.connect("database/big_app.db")

cr = db.cursor()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# cr.execute("INSERT INTO skills (name, progress, user_id) VALUES('C++', '87', 2)")
# cr.execute("INSERT INTO skills VALUES('C++', '87', 2)") # بضيف نفس العدد للفيم valuesلاني في ال (name, progress, user_id) ممكن بدون 

# لتجنب الإختراقات لقاعدة البيانات وزيادة الحماية في برنامجي لا يفضل استخدام الطريقة السابقة في اضافة بيانات مستخدم خوفا من الإختراق
# اسم هذا الاختراق هو حقن قاعدة البيانات، وبالإنجليزية
# SQL Injection
# يحدث عندما يكتب المستخدم نصا خبيثا، فيصبح جزءا من أمر قاعدة البيانات نفسه
# الحل هو الطريقة التالية: نضع علامة ? مكان كل قيمة، ونرسل القيم وحدها في tuple
# هكذا تتعامل المكتبة مع القيم كبيانات فقط، ولا يمكن أن تتحول إلى أوامر

# my_tuple = ('Pascal', 91, 4)

# cr.execute("INSERT INTO skills VALUES(?, ?, ?)",my_tuple)

# OR

# cr.execute("INSERT INTO skills VALUES(?, ?, ?)",('Pascal', 33, 1))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ملاحظة: كل استعلام يلغي ناتج الاستعلام الذي قبله
# لذلك الطباعة في آخر الملف تعرض ناتج آخر استعلام فقط
# لتجربة أي استعلام، ضع علامة # أمام الاستعلامات الأخرى
# والنواتج المكتوبة تحت كل استعلام تعتمد على البيانات التي أضفتها في الدروس السابقة

cr.execute("SELECT * FROM skills order by user_id asc") # هان برتب حسب رقم المستخدم هيطبع مهارات الشخص الاول بعدها الثاني وهكذا

# asc ->  (افتراضي ,اختياري) لترتيب التصاعدي
# desc -> (اختياري)          لترتيب التنازلي

# Output:

# Skill Name => Mysql, Skill Progress => 92, User ID => 1
# Skill Name => Css, Skill Progress => 92, User ID => 1
# Skill Name => Sqli, Skill Progress => 34, User ID => 1
# Skill Name => Php, Skill Progress => 99, User ID => 2
# Skill Name => Java, Skill Progress => 88, User ID => 2
# Skill Name => Pascal, Skill Progress => 78, User ID => 3
# Skill Name => Pascal, Skill Progress => 91, User ID => 4

cr.execute("SELECT * FROM skills order by name desc") #  هان برتب حسب اسم المهارة بترتيب تنازلي

# Output:

# Skill Name => Sqli, Skill Progress => 34, User ID => 1
# Skill Name => Php, Skill Progress => 99, User ID => 2
# Skill Name => Pascal, Skill Progress => 78, User ID => 3
# Skill Name => Pascal, Skill Progress => 91, User ID => 4
# Skill Name => Mysql, Skill Progress => 92, User ID => 1
# Skill Name => Java, Skill Progress => 88, User ID => 2
# Skill Name => Css, Skill Progress => 92, User ID => 1

cr.execute("SELECT * FROM skills order by name limit 2") #  هان برتب حسب اسم المهارة وبجلب بمقدار مهارتين فقط

# Output:

# Skill Name => Css, Skill Progress => 92, User ID => 1
# Skill Name => Java, Skill Progress => 88, User ID => 2

cr.execute("SELECT * FROM skills order by name limit 3 offset 2") #  وبجلب بمقدار ثلاث مهارات من بعد أول مهارتين

# Output:

# Skill Name => Mysql, Skill Progress => 92, User ID => 1
# Skill Name => Pascal, Skill Progress => 78, User ID => 3
# Skill Name => Pascal, Skill Progress => 91, User ID => 4

cr.execute("SELECT * FROM skills where user_id > 1")  # الهم اكبر من واحد user_idاجلب المهارات الخاصة للمستخدمين ال

# Output:

# Skill Name => Php, Skill Progress => 99, User ID => 2
# Skill Name => Java, Skill Progress => 88, User ID => 2
# Skill Name => Pascal, Skill Progress => 78, User ID => 3
# Skill Name => Pascal, Skill Progress => 91, User ID => 4

cr.execute("SELECT * FROM skills where user_id in (2, 3)")  # (2 or 3) الهم user_idاجلب المهارات الخاصة للمستخدمين ال

# Output:

# Skill Name => Php, Skill Progress => 99, User ID => 2
# Skill Name => Java, Skill Progress => 88, User ID => 2
# Skill Name => Pascal, Skill Progress => 78, User ID => 3

cr.execute("SELECT * FROM skills where user_id not in (1, 2, 3)")  # (1 or 2 or 3) الهم ليس user_idاجلب المهارات الخاصة للمستخدمين ال

# Output:

# Skill Name => Pascal, Skill Progress => 91, User ID => 4

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

results = cr.fetchall()

for row in results:

    print(f"Skill Name => {row[0]},", end=" ")
    print(f"Skill Progress => {row[1]},", end=" ")
    print(f"User ID => {row[2]}")

db.commit()

db.close()
