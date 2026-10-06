# Lesson 079 - Date And Time Introduction
# Video: https://www.youtube.com/watch?v=NH7Qd1_IGqM

# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

print(dir(datetime))
print(dir(datetime.datetime))

# Print The Current Date and Time

print(datetime.datetime.now()) # 2026-03-07 21:02:39.387503

# Print The Current Date

print(datetime.datetime.now().date()) # 2026-03-07

# Print The Current Year

print(datetime.datetime.now().year) # 2026

# Print The Current Month

print(datetime.datetime.now().month) # 3

# Print The Current Day

print(datetime.datetime.now().day) # 7

# Print Start and End Of Date

print(datetime.datetime.min) # 0001-01-01 00:00:00
print(datetime.datetime.max) # 9999-12-31 23:59:59.999999

# Print The Current Time

print(datetime.datetime.now().time()) # 21:07:44.844877

# Print The Current Time Hour

print(datetime.datetime.now().hour) # 21

# Print The Current Time Minute

print(datetime.datetime.now().minute) # 07

# Print The Current Time Second

print(datetime.datetime.now().second) # 44

# Print Start and End Of Time

print(datetime.time.min) # 00:00:00
print(datetime.time.max) # 23:59:59.999999

# Print Specific Date

print(datetime.datetime(2000, 5, 20)) # 2000-05-20 00:00:00
print(datetime.datetime(2000, 5, 20, 10, 22, 43,34243)) # 2000-05-20 10:22:43.034243

# Example ...

myBirthDay = datetime.datetime(2000, 5, 20, 10, 22, 43)
dateNow = datetime.datetime.now()

print(f"My BirthDay Is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

# My BirthDay Is 2000-05-20 10:22:43 And Date Now Is 2026-03-07 21:20:41.067567
# الناتج التالي محسوب بتاريخ 2026-03-07، وسيختلف عندك حسب تاريخ اليوم

print(f"I Lived For {dateNow - myBirthDay}") # I Lived For 9422 days, 10:57:58.067567

print(f"I Lived For {(dateNow - myBirthDay).days}") # I Lived For 9422
