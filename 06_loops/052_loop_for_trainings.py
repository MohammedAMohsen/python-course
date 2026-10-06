# Lesson 052 - Loop For Training's
# Video: https://www.youtube.com/watch?v=9JJDDKj_tGA

# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

# myRange = range(1, 100) # -> العدد من 1 ل 99

# for number in myRange:

#     print(number)


mySkills = {
    "Html" : "90%",
    "Css" : "60%",
    "PHP" : "70%",
    "JS" : "80%",
    "Python" : "95%"
}

print(mySkills['JS']) # 80%
print(mySkills.get('Python')) # 95%

for skill in mySkills:

#    print(skill)

# Html
# Css
# PHP
# JS
# Python

    print(f"My Progress In Lang {skill} Is: {mySkills[skill]}")

# My Progress In Lang Html Is: 90%
# My Progress In Lang Css Is: 60%
# My Progress In Lang PHP Is: 70%
# My Progress In Lang JS Is: 80%
# My Progress In Lang Python Is: 95%
