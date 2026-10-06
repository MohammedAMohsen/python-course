# Lesson 040 - Practical - Your Age Full Details
# Video: https://www.youtube.com/watch?v=S6dhvob-4DM

# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age

age = int(input('What\'s Your Age ? ').strip()) # عشان العمر يطلع معي عدد من نص

print(f"{age} Years")
# print(type(age)) <class 'int'>

# Get Age in All Time Units
months = age * 12
week = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:')
print(f"{months} Months.")
print(f"{week:,} Week.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")
