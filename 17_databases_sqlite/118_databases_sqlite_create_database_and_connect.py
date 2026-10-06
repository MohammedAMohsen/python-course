# Lesson 118 - Databases - SQLite Create Database And Connect
# Video: https://www.youtube.com/watch?v=UokVrMqeu4o

# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# Import SQLite Module

import sqlite3

# Create Database And Connect

db = sqlite3.connect(r"database/app.db") # إذا لم يكن الملف موجودا ينشئه تلقائيا

# Create The Tables and Fields

db.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# بعد ما اعمل تشغيل للبرنامج هينشأ قاعدة البيانات تبعتي بالجدول الي انا مسميه بالاعمدة الخاصة بيه
# لانه هيحاول ينشئ جدولا موجودا سابقا Error اذا رجعت وعملت تشغيل هيعطيني 
# قبل اسم الجدول if not exists عشان اتجاوز هذة المشكلة بضيف الجملة 
# بمعنى انو لو الجدول مش موجود أنشأة


# Close Database

db.close()
