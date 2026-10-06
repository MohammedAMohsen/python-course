# Assignment 01

def get_score(**skills):
    for skill_key, skill_value in skills.items():
        print(f"{skill_key} => {skill_value}")

get_score(Math=90, Science=80, Language=70)
# _______________________________________________________________________________________________________
# Assignment 02

def get_the_scores(Name="", **Skills):
    if Skills:
        if Name:
            print(f"Hello {Name} This Is Your Score Table:")
        for skill_key, skill_value in Skills.items():
            print(f"{skill_key} => {skill_value}")
    else:
        print(f"Hello {Name} You Have No Scores To Show")

get_the_scores("Osama", Math=90, Science=80, Language=70)
get_the_scores("Mahmoud", Logic=70, Problems=60)
get_the_scores(Logic=70, Problems=60)
get_the_scores("Ahmed")
# _______________________________________________________________________________________________________
# Assignment 03

scores_list = {
    "Math" : "90%",
    "Science" : "80%",
    "Language" : "70%"
}

def get_the_scores(Name="", **Skills):
    if Skills:
        if Name:
            print(f"Hello {Name} This Is Your Score Table:")
        for skill_key, skill_value in Skills.items():
            print(f"{skill_key} => {skill_value}")
    else:
        print(f"Hello {Name} You Have No Scores To Show")

get_the_scores("Osama", **scores_list)
get_the_scores("Ahmed")
get_the_scores(**scores_list)
