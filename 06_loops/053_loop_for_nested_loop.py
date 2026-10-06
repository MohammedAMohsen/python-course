# Lesson 053 - Loop For Nested Loop
# Video: https://www.youtube.com/watch?v=x_GyjV2Nb6k

# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'Js']

# for name in peoples: # Outer Loop

#     print(f"{name} Skills Is: ")

#     for skill in skills: # Inner Loop

#         print(f"- {skill}")

# Osama Skills Is: 
# - Html
# - Css
# - Js
# ...

# Dictionary

peoples = {
    "Osama": {
        "Html": "70%",
        "Css": "80%",
        "Js": "70%"
    },
    "Ahmed": {
        "Html": "90%",
        "Css": "80%",
        "Js": "90%"
    },
    "Sayed": {
        "Html": "70%",
        "Css": "60%",
        "Js": "90%"
    }
}

# print(peoples["Ahmed"]) # {'Html': '90%', 'Css': '80%', 'Js': '90%'}
# print(peoples["Ahmed"]["Html"]) # 90%
# print(peoples["Ahmed"]["Css"]) # 80%
# print(peoples["Ahmed"]["Js"]) # 90%

for name in peoples:

#   print(name)
# Osama
# Ahmed
# Sayed

#   print(f"Skills and Progress For {name} Is: {peoples[name]}")

# Skills and Progress For Osama Is: {'Html': '70%', 'Css': '80%', 'Js': '70%'}
# Skills and Progress For Ahmed Is: {'Html': '90%', 'Css': '80%', 'Js': '90%'}
# Skills and Progress For Sayed Is: {'Html': '70%', 'Css': '60%', 'Js': '90%'}

    print(f"Skills and Progress For {name} Is: ")

    for skill in peoples[name]:

        print(f"{skill.upper()} => {peoples[name][skill]}")

# Skills and Progress For Osama Is: 
# HTML => 70%
# CSS => 80%
# JS => 70%
# Skills and Progress For Ahmed Is: 
# HTML => 90%
# CSS => 80%
# JS => 90%
# Skills and Progress For Sayed Is: 
# HTML => 70%
# CSS => 60%
# JS => 90%
