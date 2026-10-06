# Lesson 065 - Files Handling Part One Intro
# Video: https://www.youtube.com/watch?v=6TFJs9uzEjI

# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

# file = open(r"C:\Python\files\mode.txt")

# r ?? -> عشان يفهم إنو الي بعد الشرطة إسم ملف وليس حروف خاصة
# هذا الحرف يجعل النص خاما، فلا تعامل الشرطة المائلة كرمز هروب
# بدونه يفهم بايثون أن \f مثلا رمز خاص، فيصبح المسار خاطئا

# طرف ثانية عشان أجيب مسار الملف , يمكن تكون معقدة فهعتمد الطريقة الأولى

# import os

# Main Current working Directory
# print(os.getcwd()) # C:\Python -> برجع المسار الى أنا فيه حاليا

# Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__))) # C:\Python\08_files_handling

# Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd()) # C:\Python\08_files_handling

# print(os.path.abspath(__file__)) # C:\Python\08_files_handling\065_files_handling_part_1_intro.py



# المسار هنا يبدأ من المجلد الرئيسي للدورة، لذلك شغل الملف وأنت داخل هذا المجلد
file = open("files/mode.txt","w")
file.close()

import os

print(os.getcwd()) # /home/user/python-course
print(os.path.abspath(__file__)) # /home/user/python-course/08_files_handling/065_files_handling_part_1_intro.py
print(os.path.dirname(os.path.abspath(__file__))) # /home/user/python-course/08_files_handling
# os.chdir()

