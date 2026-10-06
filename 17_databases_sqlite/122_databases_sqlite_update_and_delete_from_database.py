# Lesson 122 - Databases - SQLite Update And Delete From Database
# Video: https://www.youtube.com/watch?v=8B9EZt-4980

# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module:

import sqlite3

# Create Database And Connect:

db = sqlite3.connect(r"database/app.db")

# Setting Up The Cursor:

cr = db.cursor()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Update Data:

cr.execute("update users set name = 'Mostafa' where user_id = 101")
cr.execute("update users set name = 'Kamal' where user_id = 102")
cr.execute("update users set name = 'Ali' where user_id = 103")

# Fetch Data After Update:

cr.execute("select * from users")

# البيانات بعد التحديث
print(cr.fetchone()) # (101, 'Mostafa')
print(cr.fetchone()) # (102, 'Kamal')
print(cr.fetchone()) # (103, 'Ali')
print(cr.fetchone()) # None

# -----------------------------------------

# Delete Data:

# cr.execute("delete from users") هيك بحذف جميع الحقول داخل الجدول

cr.execute("delete from users where user_id = 102") # (user_id = 102)هيك بحذف الحقل صاحب ال


# Fetch Data After Delete:

cr.execute("select * from users")

# البيانات بعد إجرائ الحذف
print(cr.fetchone()) # (101, 'Mostafa')
print(cr.fetchone()) # (103, 'Ali')
print(cr.fetchone()) # None

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Save (Commit) Changes:

db.commit()

# Close Database:

db.close()


