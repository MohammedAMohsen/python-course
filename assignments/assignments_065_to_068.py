# Assignment 01

import os

# المجلد الذي سنحفظ فيه الملفات، ننشئه إذا لم يكن موجودا
os.makedirs("assignments/files", exist_ok=True)

for file in range(1,51):
    if file != 25:
        myFile = open(f"assignments/files/txt{str(file).zfill(2)}.txt","w")
        myFile.write(f"Elzero Web School => File: {file}\n")
    else:
        myFile = open("assignments/files/special-text.txt","w")
    myFile.close()

print(os.getcwd()) # /home/user/python-course
print(os.path.dirname(os.path.abspath(__file__))) # /home/user/python-course/assignments
print(os.path.abspath(__file__)) # /home/user/python-course/assignments/assignments_065_to_068.py
print(len(os.listdir("assignments/files"))) # 50

# _______________________________________________________________________________________________________
# Assignment 02

myFile = open("assignments/files/txt01.txt", "a")
myFile.write("Appended => Elzero Web School\n" * 50)
myFile.close() # لازم نغلق الملف حتى تحفظ الكتابة قبل أن نقرأه

# _______________________________________________________________________________________________________
# Assignment 03
myFile = open("assignments/files/txt01.txt","r")

# نقرأ المحتوى مرة واحدة ونحفظه في متغير
# لأن القراءة الثانية من نفس الملف ترجع نصا فارغا، فالمؤشر وصل لآخر الملف
content = myFile.read()
myFile.close()

print(f"Number Of Lines Is => {len(content.splitlines())}") # Number Of Lines Is => 51

print(f"Number Of Words Is => {len(content.split())}") # Number Of Words Is => 256

print(f"Number Of 'l' Char Is => {content.count('l')}") # Number Of 'l' Char Is => 103

i = 0
for word in content.split():
    i += len(word)
print(f"Number Of Chars Is => {i}") # Number Of Chars Is => 1273

# _______________________________________________________________________________________________________
# Assignment 04

myFile = sorted(os.listdir("assignments/files")) # sorted -> نرتب الأسماء لأن ترتيب listdir غير مضمون
myFile.reverse()
for file in myFile[:10]:
    os.remove(f"assignments/files/{file}")

# تم حذف آخر 10 ملفات
