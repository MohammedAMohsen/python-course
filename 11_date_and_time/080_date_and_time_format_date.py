# Lesson 080 - Date And Time Format Date
# Video: https://www.youtube.com/watch?v=Qa6p-eQ7k0U

# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------
import datetime

myBirthDay = datetime.datetime(2000, 5, 20)

print(myBirthDay) # 2000-05-20 00:00:00

print(myBirthDay.strftime("%a")) # Sat
print(myBirthDay.strftime("%A")) # Saturday
print(myBirthDay.strftime("%b")) # May
print(myBirthDay.strftime("%B")) # May

print(myBirthDay.strftime("%d %B %Y")) # 20 May 2000
print(myBirthDay.strftime("%d-%b-%y")) # 20-May-00

# نفس الطريقة للوقت والساعة بنفس الفكرة ارجع لرابط الذي بالأعلى لمعرفة جميع الإختصارات


