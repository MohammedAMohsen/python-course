# Extra: Connect To MySQL (my own practice, not a video lesson)
# مثال إضافي للاتصال بقاعدة بيانات MySQL بدلا من SQLite

# أمر التثبيت من الطرفية
# pip install mysql-connector-python

import os
import mysql.connector

# لا تكتب كلمة المرور الحقيقية داخل الكود أبدا، خاصة إذا كنت سترفعه على الإنترنت
# الأفضل قراءتها من متغير في النظام، قبل التشغيل اكتب في الطرفية
# export MYSQL_PASSWORD="your_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    # database="ecom"
)

print("Connected The Database Successfully :) ")

cr = db.cursor()
