# Lesson 101 - Regular Expressions Part 7 Re Module Split & Sub
# Video: https://www.youtube.com/watch?v=ZGizsqwe4ps

# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------

# =======================================
#                split() قطع
# =======================================

import re

string_one = "I Love Python Programming-Language"

search_one1 = re.split(r"\s", string_one)

print(search_one1) # ['I', 'Love', 'Python', 'Programming-Language'] 

search_one2 = re.split(r"\s", string_one, 1)

print(search_one2) # ['I', 'Love Python Programming-Language'] 

# ---------------------------------------------------------------

string_two = "How-To_Write_A_Very-Good-Article"

search_two1 = re.split(r"-", string_two)

print(search_two1) # ['How', 'To_Write_A_Very', 'Good', 'Article']

search_two2 = re.split(r"-|_", string_two)

print(search_two2) # ['How', 'To', 'Write', 'A', 'Very', 'Good', 'Article']

# ---------------------------------------------------------------

# Get Words From URL

for coun, word in enumerate(search_two2, 1):

    # (a)هاد الشرط عشان ما أطبع الكلمات المكونة من حرف واحد مثل ال
    if len(word) > 1:
        print(f"{coun}- {word.lower()}")

# Output

# 1- how
# 2- to
# 3- write
# 5- very
# 6- good
# 7- article

# =======================================
#                sub() الإستبدال
# =======================================


myString = "I Love Python Programming Language"

print(re.sub(r"\s"," @ ", myString)) # I @ Love @ Python @ Programming @ Language
print(re.sub(r"\s"," @ ", myString, 2)) # I @ Love @ Python Programming Language
