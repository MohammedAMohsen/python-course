# Lesson 120 - Databases - SQLite Retrieve Data From Database
# Video: https://www.youtube.com/watch?v=vYkNQmwGTpQ

# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) => returns the next (size) rows as a list of tuples.
# ------------------------------------------------------

# Import SQLite Module:

import sqlite3

# Create Database And Connect:

db = sqlite3.connect(r"database/app.db")

# Setting Up The Cursor:

cr = db.cursor()

# Create The Tables and Fields:

cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data:

# cr.execute("insert into users(user_id, name) values(101, 'Mohammed')")
# cr.execute("insert into users(user_id, name) values(102, 'Osama')")
# cr.execute("insert into users(user_id, name) values(103, 'Ahmed')")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Fetch Data:

cr.execute("select name from users")

print(cr.fetchone()) # ('Mohammed',)
print(cr.fetchone()) # ('Osama',)
print(cr.fetchone()) # ('Ahmed',)
print(cr.fetchone()) # None

print(cr.fetchall()) # []
# الناتج قائمة فارغة لأني جلبت كل الأسماء سابقا بالأمر fetchone
# لو استخدمتها أول مرة بعد الاستعلام مباشرة، يكون الناتج هكذا
# [('Mohammed',), ('Osama',), ('Ahmed',)]

# -------------------------

cr.execute("select user_id, name from users")

print(cr.fetchall()) # [(101, 'Mohammed'), (102, 'Osama'), (103, 'Ahmed')]

# -------------------------

cr.execute("select * from users") # -> تعني كل الحقول (*)

print(cr.fetchall()) # [(101, 'Mohammed'), (102, 'Osama'), (103, 'Ahmed')]

# -------------------------

cr.execute("select * from users")

print(cr.fetchmany(2)) # [(101, 'Mohammed'), (102, 'Osama')] # -> برجع أول صفين (سجلين) فقط

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Save (Commit) Changes:

db.commit()

# Close Database:

db.close()


