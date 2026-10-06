# Assignment 01/02/03/04/05

import sqlite3

db = sqlite3.connect("database/albasha.db")

cr = db.cursor()

cr.execute("create table if not exists users(id integer primary key, name text , dob text, email text UNIQUE)")

users = [(1, 'Ahmed', '20/10/1980', 'ahmed@example.com'),
         (2, 'Mohsen', '04/03/2010', 'mohsen@example.com'),
         (3, 'Gamal', '14/12/1990', 'Gamal@example.com'),
         (4, 'Sayed', '22/05/1987', 'sayed@example.com'),
         (5, 'Sameh', '30/02/2000', 'Sameh@example.com'),
         (6, 'Mona', '19/05/2004', 'mona@example.com')]

# السؤال: ضيف المستخدمين اذا كان موجود المستخدم مسبقا ما اضيفو

# ----------------
# الطريقة الاولى
# ----------------

# try:

#     for user in users:
        
#         cr.execute(f"select * from users where id = {user[0]}")

#         if cr.fetchone() == None:

#             cr.execute("INSERT INTO users(id, name, dob, email) values(?,?,?,?)", user)

# except sqlite3.Error as er:

#     print(er)

# ----------------
# الطريقة الثانية
# ----------------

# for user in users:
        
#     try:

#         cr.execute("INSERT INTO users(id, name, dob, email) values(?,?,?,?)", user)

#     except sqlite3.Error as er:

#         pass

# ----------------
# الطريقة الثالثة والأفضل
# ----------------

for user in users:

    cr.execute("INSERT OR IGNORE INTO users(id, name, dob, email) values(?,?,?,?)", user)

# ---------------------------------------

# بهاي الطرق الثلاث في حال اضفت مستخدم جديد في القائمة
# وشغلت البرنامج بعدي عن كل المستخدمين وما بضيفهم وبضيف المستخدم الجديد فقط

# IGNORE INTO والطريقة الثالثة هي الأفضل في الحالة الي عندي

# :شرح الطريقة الثالثة
# البرنامج بحاول يضيف كل المستخدمين في القائمة
# يتجاهل هذا المستخدم (id or email مكرر)اذا المستخدم موجود
# اذا المستخدم جديد مثل الشخص السادس بنضاف بدون مشاكل
# البرنامج يكمل بدون اي خطأ او توقف

# ---------------------------------------

# في الجدول Row السؤال: قم بجلب آخر

cr.execute(f"select * from users order by id desc limit 1")

result = cr.fetchone()

print(result) # (6, 'Mona', '19/05/2004', 'mona@example.com')

# ---------------------------------------

delete_user = input("Enter The User ID To Delete: ")

# نستخدم علامة ? لأن القيمة جاية من المستخدم، حماية من حقن قاعدة البيانات (الدرس 127)
cr.execute("select * from users where id = ?", (delete_user,))

if cr.fetchone() != None:

    cr.execute("Delete from users where id = ?", (delete_user,))

    print("User Deleted Successfully.")

    cr.execute("select * from users")

    for row in cr.fetchall():

        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")

else:

    print("User Not Found :(")

# Output:

# Enter The User ID To Delete: 3
# User Deleted Successfully.
# ID => 1, Name => Ahmed, Date Of Birth => 20/10/1980, Email => ahmed@example.com
# ID => 2, Name => Mohsen, Date Of Birth => 04/03/2010, Email => mohsen@example.com
# ID => 4, Name => Sayed, Date Of Birth => 22/05/1987, Email => sayed@example.com
# ID => 5, Name => Sameh, Date Of Birth => 30/02/2000, Email => Sameh@example.com
# ID => 6, Name => Mona, Date Of Birth => 19/05/2004, Email => mona@example.com

# ---------------------------------------

db.commit()

db.close()
