# Lesson 055 - Loop Advanced Dictionary
# Video: https://www.youtube.com/watch?v=zTLmupb3cKg

# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

# print(mySkills.items()) # dict_items([('HTML', '80%'), ('CSS', '90%'), ('JS', '70%'), ('PHP', '80%')])

# for skill in mySkills:
    
#     print(f"{skill} => {mySkills[skill]}")

# HTML => 80%
# CSS => 90%
# JS => 70%
# PHP => 80%

# for skill_key, skill_progress in mySkills.items():

#     print(f"{skill_key} => {skill_progress}")

# HTML => 80%
# CSS => 90%
# JS => 70%
# PHP => 80%

myUltimateSkills = {
    "Html" : {
        "Main" : "80%",
        "Pugjs" : "78%",
    },
    "CSS" : {
        "Main" : "90%",
        "Sass" : "60%"
    }
}

for main_key, main_value in myUltimateSkills.items():
    
  print(f"{main_key} Progress Is: ")

# Html
# CSS

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")
  
# Html Progress Is: 
# - Main => 80%
# - Pugjs => 78%
# CSS Progress Is: 
# - Main => 90%
# - Sass => 60%
