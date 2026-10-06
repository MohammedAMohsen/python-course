# Lesson 068 - Files Handling Part 4 Important Info
# Video: https://www.youtube.com/watch?v=wwe40Ngpp3A

# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

# myFile = open("files/Mohammed.txt", "a")

# Mohammed.txt ...
# Hello From Python File With Love

# myFile.truncate(5) # بيبقي أول 5 أحرف من الملف وبحذف الباقي
# Mohammed.txt ...
# Hello


# myFile = open("files/Mohammed.txt", "a")

# print(myFile.tell()) # 5 #-> بقلي المؤشر وين واقف بالزبط في الملف


# Mohammed.txt ...
# Hello From Python File With Love

myFile = open("files/Mohammed.txt", "r")

myFile.seek(11) #-> بعدل مكان المؤشر (هان وضعتو على بعد 11 حرف) وببدأ يقرأ من بعدو

print(myFile.read()) # Python File With Love
myFile.close()


# Delete File:

# import os
# os.remove("files/Mohammed.txt")

# The Better Way To Open Files: with
# الطريقة الأفضل لفتح الملفات هي استخدام with
# لأنها تغلق الملف تلقائيا عند الخروج منها، حتى لو حدث خطأ

with open("files/Mohammed.txt", "r") as myFile:
    print(myFile.readline()) # Hello From Python File With Love

print(myFile.closed) # True -> الملف أغلق تلقائيا
