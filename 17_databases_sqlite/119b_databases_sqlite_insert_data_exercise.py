# Extra exercise for lesson 119 (my own practice, not a video lesson)
# Lesson 119 video: https://www.youtube.com/watch?v=JCjGtiKCYO4

# -----------------------------------------------
# --------------- تمرين متقدم--------------------
# -----------------------------------------------

# قم بإنشاء قاعدة بيانات مستخدمين وأنشاء جدول يحتوى على اسماء الأشخاص التي في القائمة مع اعطاء كل شخص معرف خاص رقم 

my_list = ["Ahmed", "Ibrahim", "Mohammed", "Ali", "Abood", "Kamel", "Mona"]

import sqlite3

db = sqlite3.connect(r"database/Exercise_Insert.db")

cr = db.cursor()

cr.execute("create table if not exists users (user_id integer, name text)")

for key, user in enumerate(my_list, 101):

    cr.execute(f"insert into users(user_id, name) values({key}, '{user}')")

db.commit()

db.close()
