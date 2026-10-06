# Lesson 061 - Function Packing Unpacking Arguments Training's
# Video: https://www.youtube.com/watch?v=7o58LMti2po

# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("Html", "Css", "Js")

mySkills = {
    "Go" : "80%",
    "Dart" : "50%",
    "Java" : "95%",
    "Python" : "84%",
    "MySQL" : "40%"
}

def show_skills(name, *skills, **skillsWithProgress):

    print(f"Hello {name} \nSkills Without Progress Is:")

    for skill in skills:

        print(f"- {skill}")
    
    print("Skills With Progress Is: ")

    for skill_key, skill_value in skillsWithProgress.items():

        print(f"- {skill_key} => {skill_value}")

show_skills("Mohammed", "Html", "Css", "Js", python = "95%", Java = "94%")

# Hello Mohammed 
# Skills Without Progress Is:
# - Html
# - Css
# - Js
# Skills With Progress Is:
# - python => 95%
# - Java => 94%

show_skills("AlBasha", *myTuple, **mySkills)

# Hello AlBasha 
# Skills Without Progress Is:
# - Html
# - Css
# - Js
# Skills With Progress Is: 
# - Go => 80%
# - Dart => 50%
# - Java => 95%
# - Python => 84%
# - MySQL => 40%
