# Lesson 119 - Databases - SQLite Insert Data Into Database
# Video: https://www.youtube.com/watch?v=JCjGtiKCYO4

# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------

# Import SQLite Module

import sqlite3

# Create Database And Connect

db = sqlite3.connect(r"database/app.db")

# Setting Up The Cursor

cr = db.cursor()

# Create The Tables and Fields

cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data

cr.execute("insert into users(user_id, name) values(101, 'Mohammed')")
cr.execute("insert into users(user_id, name) values(102, 'Osama')")
cr.execute("insert into users(user_id, name) values(103, 'Ahmed')")

# Save (Commit) Changes -> هذا الأمر مهم جدا جدا عشان يحفظ التغيرات الي أجريتها على قاعدة البيانات وتظهر عندي بدون مشاكل

db.commit() # -> بعد هذا الأمر هيضيف البيانات داخل جدول المستخدمين لثلاث مستخدمين
# ملاحظة: كل تشغيل جديد لهذا الملف يضيف نفس المستخدمين الثلاثة مرة أخرى

# Close Database

db.close()


