# Lesson 066 - Files Handling Part 2 Read Files
# Video: https://www.youtube.com/watch?v=9ZU9FQQbOYE

# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile1 = open("files/text1.txt", "r")
myFile2 = open("files/text2.txt", "r")
myFile3 = open("files/text3.txt", "r")

# التعليمات البرمجية عادي بترجع معلومات حول الملف
# print(myFile1) # File Data Object \\ <_io.TextIOWrapper name='files/text1.txt' mode='r' encoding='UTF-8'>
# print(myFile1.name) # files/text1.txt
# print(myFile1.mode) # r
# print(myFile1.encoding) # UTF-8 -> على ويندوز قد يظهر cp1252 أو cp65001

# print(myFile1.read()) # Default value -> read() => Mohammed Alaa Mohsen بقرأ جميع محتويات الملف 
# print(myFile1.read(11))

# لاحظ في المرة الثانية عندما طلبت منه أن يقرأ ما طبع إشي؟
# لأن في الخطو الي قبل قرأت وطبعت جميع محتوى الملف فمش هيلاقي إشي يقرأو
# !!! لاحظ السناريو القادم

# print(myFile2.read(12)) # Mohammed Ala
# print(myFile2.read(5)) # a Moh
# print(myFile2.read()) # sen -->  إيش ضايل في أشي ما إنقرأ إقرأو وكمل للآخر

# بقرأ سطر سطر
# print(myFile3.readline()) # Mohammed Alaa Mohsen
# print(myFile3.readline()) # ALBasha 123456789 GG In The Years
# print(myFile3.readline(11)) # Mohammed Al -> هيقرأ أول 11 حرف من السطر الأول أو للسطر الى وصل لإلو في القراءة

# بقرأ الأسطر سطر سطر وبرجعم كقائمة
# print(myFile3.readlines()) # ['Mohammed Alaa Mohsen\n', 'ALBasha 123456789 GG In The Years\n', 'Super Developer']
# print(myFile3.readlines(20)) # ['Mohammed Alaa Mohsen\n'] 
# print(type(myFile3.readlines())) # <class 'list'>

# for line in myFile3:
    # print(line)

# Mohammed Alaa Mohsen
# ALBasha 123456789 GG In The Years
# Super Developer


for line in myFile3:
    print(line)
    if line.startswith("ALBasha"):
        break

# Mohammed Alaa Mohsen
#
# ALBasha 123456789 GG In The Years
# بين السطرين سطر فارغ لأن كل سطر في الملف ينتهي بـ \n والطباعة تضيف سطرا جديدا أيضا

# Close The File

myFile1.close()
myFile2.close()
myFile3.close()
