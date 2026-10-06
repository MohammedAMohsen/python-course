# Lesson 067 - Files Handling Part 3 Write and Append In Files
# Video: https://www.youtube.com/watch?v=FBcElrNaiZQ

# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

# myFile = open("files/Mohammed.txt", "w") # لو الملف مش موجود هينشئو بشكل تلقائي

# لو غيرت في الكتابة هيمسح الموجود ويكتب فوقه
# myFile.write("Hello From Python File With Love\n")
# myFile.write("Second Line")

# Mohammed.txt ...
# Hello From Python File With Love
# Second Line

# myFile = open("files/fun.txt", "w")
# myFile.write("AlBasha Web School\n" * 100)

# fun.txt ...
# AlBasha Web School
# AlBasha Web School
# AlBasha Web School
# AlBasha Web School
# ...
# 100

# myList = ["Mohammed", "Alaa", "Abd", "Sayed", "Hasen"]
# myFile = open("files/friends.txt", "w")

# for friend in myList:
#     myFile.write(friend+"\n")


# friends.txt ...
# Mohammed
# Alaa
# Abd
# Sayed
# Hasen

# Append In File: => في آخر سطر كان مكتوب \n بضيف على الملف , ما بمسح المحتوى القديم , بكتب بعدو عطول بالزق إلى اذا كان فيه

myFile = open("files/friends.txt", "a") # لو الملف مش موجود هينشئو بشكل تلقائي

myFile.write("Hello\n")
myFile.write("Second Line")
myFile.write("line Testing\n")
myFile.write("line Testing\n\n\n")
myFile.write("final")
myFile.close() # إغلاق الملف بعد الانتهاء يضمن حفظ كل ما كتبناه

# friends.txt ...
# Mohammed
# Alaa
# Abd
# Sayed
# Hasen
# Hello
# Second Lineline Testing
# line Testing


# final |...
