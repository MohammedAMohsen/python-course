# Lesson 060 - Function Packing Unpacking Keyword Arguments
# Video: https://www.youtube.com/watch?v=pMeKs94OrxQ

# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills):
#     for skill in skills:
#         print(f"{skill}")

# show_skills("Html", "Css","js")

mySkills = {
    "Html" : "80%",
    "Sass" : "50%",
    "Java" : "95%",
    "Python" : "84%",
    "MySQL" : "40%"
}

def show_skills(**skills): # -> ** Dictionary

    print(type(skills)) # <class 'dict'>

    for skill, value in skills.items():

        print(f"{skill} => {value}")

show_skills(Html = 80, Css = 70, js = 93)
# Html => 80
# Css => 70
# js => 93

# print(**mySkills) Error -> عشان يعرف يقرأها Functionلازم إدخالها على ال
# show_skills(mySkills) Error
show_skills(**mySkills) # عشان أضيف قاموس خارجي لازم أفكفكو يعني أضيف النجمتين قبلو زي هيك

# Html => 80%
# Sass => 50%
# Java => 95%
# Python => 84%
# MySQL => 40%
