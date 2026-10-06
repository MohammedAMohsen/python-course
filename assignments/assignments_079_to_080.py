# Assignment 01

import datetime

TheDate = datetime.datetime(2021, 6, 25).date() 
DateNow = datetime.datetime.now().date()

print(f"Days From {TheDate} To {DateNow} Is => {(DateNow - TheDate).days}")

# Days From 2021-06-25 To 2026-03-07 Is => 1716

# _______________________________________________________________________________________________________
# Assignment 02

print(datetime.datetime.now().date()) # 2026-03-07
print(datetime.datetime.now().strftime("%b %d, %Y")) # Mar 07, 2026
print(datetime.datetime.now().strftime("%d - %b - %Y")) # 07 - Mar - 2026
print(datetime.datetime.now().strftime("%d / %b / %y")) # 07 / Mar / 26
print(datetime.datetime.now().strftime("%d / %B / %Y")) # 07 / March / 2026
print(datetime.datetime.now().strftime("%a, %d / %B / %Y")) # Sat, 07 / March / 2026